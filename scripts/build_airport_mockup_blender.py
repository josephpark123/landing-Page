"""Blender material pass and batched GLB export. Run with blender --background."""
import bpy, json, math, sys, argparse
import numpy as np
from pathlib import Path
from mathutils import Vector
ROOT=Path(__file__).resolve().parents[1]
parser=argparse.ArgumentParser();parser.add_argument('source',type=Path);parser.add_argument('--build',type=Path)
options=parser.parse_args(sys.argv[sys.argv.index('--')+1:])
BUILD=(options.build or ROOT/'output/airport-mockup').resolve();OUT=BUILD/'assets';OUT.mkdir(parents=True,exist_ok=True)
source=options.source.resolve()
bpy.ops.object.select_all(action='SELECT');bpy.ops.object.delete(use_global=False)
spec=json.loads((BUILD/'geometry.json').read_text())
styles={
 'grass':('#8d9a77',.95,0),'site-edge':('#d2d4cf',.8,0),
 'apron':('#959ca0',.84,0),'shoulder':('#808683',.9,0),
 'taxiway':('#52595d',.84,0),'runway':('#3d4348',.92,0),
 'road':('#878d90',.9,0),'road-deck':('#878d90',.9,0),'road-curb':('#c5c8c7',.9,0),'parking':('#969c9b',.84,0),
 'white-marking':('#efede3',.72,0),'yellow-marking':('#e5bb46',.64,.03),
 'road-marking':('#dfded1',.8,0),'glass':('#627f85',.17,.48),
 'mullion':('#c5cecd',.34,.6),'roof':('#c4d0d8',.36,.45),
 'roof-seam':('#9aa7a7',.46,.4),'skylight':('#69868c',.16,.55),
 'building':('#a6aaad',.76,.03),'building-roof':('#bdc1c4',.65,.05),'plinth':('#b6bfba',.65,.05),
 'tower':('#c6cfcd',.46,.18),'bridge':('#c0cac8',.5,.12),
 'bridge-glass':('#6b878a',.22,.4)
}
def linear(c):return c/12.92 if c<=.04045 else ((c+.055)/1.055)**2.4
textures={}
texture_dir=source/'pages/layout_design/viewers/grid3d/assets/textures'
for kind,filebase in [('grass','sparse_grass'),('apron','concrete_pavement'),('asphalt','asphalt_02')]:
    for suffix in ['diff','nor_gl','rough']:
        image=bpy.data.images.load(str(texture_dir/(filebase+'_'+suffix+'_2k.jpg')))
        if suffix!='diff':image.colorspace_settings.name='Non-Color'
        size=512 if suffix=='rough' else 1024
        image.scale(size,size)
        image.filepath_raw=str(OUT/(kind+'-'+suffix+'.jpg'));image.file_format='JPEG';image.save()
        textures[(kind,suffix)]=image
for name,geo in spec.items():
    color,rough,metal=styles[name];rgb=[linear(int(color[i:i+2],16)/255) for i in [1,3,5]]
    mat=bpy.data.materials.new(name);mat.use_nodes=True
    p=mat.node_tree.nodes.get('Principled BSDF');p.inputs['Base Color'].default_value=(*rgb,1)
    p.inputs['Roughness'].default_value=rough;p.inputs['Metallic'].default_value=metal
    if name in ['glass','skylight','roof']:p.inputs['Coat Weight'].default_value=.2
    # Diffuse textures are connected in the web material pass with gentle tinting;
    # the portable GLB keeps compact plain PBR materials and shared world UVs.
    mesh=bpy.data.meshes.new(name);mesh.from_pydata(geo['v'],[],geo['f']);mesh.update()
    obj=bpy.data.objects.new(name,mesh);bpy.context.collection.objects.link(obj);mesh.materials.append(mat)
    # Same world-meter repeats as 260903 Grid3DMaterials.
    uv=mesh.uv_layers.new(name='WorldUV');tile=22 if name=='grass' else 10 if name in ['apron','parking'] else 14
    for loop in mesh.loops:
        v=mesh.vertices[loop.vertex_index].co;uv.data[loop.index].uv=(v.x/tile,v.y/tile)
    obj['materialGroup']=name

bpy.ops.export_scene.gltf(filepath=str(OUT/'airport.glb'),export_format='GLB',export_yup=False,export_extras=True,export_cameras=False,export_lights=False,export_apply=True)
scene=bpy.context.scene
scene.render.engine='CYCLES';scene.cycles.samples=24;scene.cycles.use_denoising=True
scene.render.resolution_x=1440;scene.render.resolution_y=960;scene.render.resolution_percentage=100
scene.world.use_nodes=True;scene.world.node_tree.nodes['Background'].inputs[0].default_value=(.78,.84,.9,1);scene.world.node_tree.nodes['Background'].inputs[1].default_value=.5
sun_data=bpy.data.lights.new('Soft afternoon sun','SUN');sun_data.energy=3;sun_data.angle=math.radians(6)
sun=bpy.data.objects.new('Soft afternoon sun',sun_data);bpy.context.collection.objects.link(sun);sun.rotation_euler=(math.radians(25),math.radians(-35),math.radians(-25))
camdata=bpy.data.cameras.new('Terminal cinematic camera');cam=bpy.data.objects.new('Terminal cinematic camera',camdata);bpy.context.collection.objects.link(cam)
cam.location=(-50,80,430);target=Vector((-660,810,15));cam.rotation_euler=(target-cam.location).to_track_quat('-Z','Y').to_euler();camdata.lens=42;camdata.clip_end=30000;scene.camera=cam
scene.render.image_settings.file_format='PNG';scene.render.filepath=str(BUILD/'blender-material-preview.png')
bpy.ops.wm.save_as_mainfile(filepath=str(BUILD/'RKSI-airport-mockup.blend'))
print('BLENDER_EXPORT',json.dumps({'bytes':(OUT/'airport.glb').stat().st_size,'objects':len(spec),'vertices':sum(len(g['v']) for g in spec.values())}))
