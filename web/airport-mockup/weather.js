/* Source-inspired day/night lighting with batched airport fixtures. */
(() => {
  'use strict';
  class AirportWeather {
    constructor({scene,renderer,ambient,hemi,sun,meta,onChange,aircraftGroups=[]}){
      Object.assign(this,{scene,renderer,ambient,hemi,sun,onChange});
      this.mode='clear';
      this.materials=[];const seen=new Set(),aircraftMaterials=new Set();
      for(const group of aircraftGroups)for(const part of group.parts)for(const mat of Array.isArray(part.mesh.material)?part.mesh.material:[part.mesh.material])aircraftMaterials.add(mat);
      scene.traverse(node=>{for(const mat of node.material?Array.isArray(node.material)?node.material:[node.material]:[]){
        if(!mat.isMeshStandardMaterial||seen.has(mat))continue;seen.add(mat);
        this.materials.push({mat,emissive:mat.emissive.clone(),emissiveIntensity:mat.emissiveIntensity,env:mat.envMapIntensity,aircraft:aircraftMaterials.has(mat)});
      }});
      this.makeNight(meta.lighting||{});
      this.makeAircraftLights(aircraftGroups,meta.tracks.length);
      this.toolbar=document.createElement('div');this.toolbar.className='weather-tools';this.toolbar.setAttribute('role','group');this.toolbar.setAttribute('aria-label','Lighting');
      this.toolbar.innerHTML='<button type="button" data-weather="night" aria-label="Night" title="Night" aria-pressed="false"><svg viewBox="0 0 24 24" aria-hidden="true"><path d="M20.5 14A9 9 0 0 1 10 3.5 9 9 0 1 0 20.5 14Z"/></svg></button>';
      this.handleClick=e=>{if(e.target.closest('button[data-weather]'))this.setMode(this.mode==='night'?'clear':'night')};
      this.toolbar.addEventListener('click',this.handleClick);document.querySelector('.navigation').appendChild(this.toolbar);
      this.setMode('clear');
    }
    makeNight(lighting){
      const colors={blue:'#269bff',green:'#42edb7',white:'#fff2d4',red:'#ff5a42',warm:'#ffd696',pbb:'#ffe0ae'},positions=[],tints=[];
      for(const [kind,list] of Object.entries(lighting)){
        if(!colors[kind])continue;
        const color=new THREE.Color(colors[kind]);
        for(let i=0;i<list.length;i+=3){positions.push(list[i],list[i+1],list[i+2]);tints.push(color.r,color.g,color.b)}
      }
      const geo=new THREE.BufferGeometry();geo.setAttribute('position',new THREE.Float32BufferAttribute(positions,3));geo.setAttribute('color',new THREE.Float32BufferAttribute(tints,3));
      this.nightLights=new THREE.Points(geo,new THREE.ShaderMaterial({transparent:true,depthWrite:false,vertexColors:true,blending:THREE.AdditiveBlending,
        vertexShader:'varying vec3 vTint;void main(){vTint=color;vec4 mv=modelViewMatrix*vec4(position,1.);gl_PointSize=clamp(5200./max(1.,-mv.z),2.2,10.);gl_Position=projectionMatrix*mv;}',
        fragmentShader:'varying vec3 vTint;void main(){float r=length(gl_PointCoord-.5);float a=exp(-r*r*68.)+exp(-r*r*13.)*.30;if(r>.5)discard;gl_FragColor=vec4(vTint,a);}'
      }));this.nightLights.visible=false;this.scene.add(this.nightLights);
      const glow=document.createElement('canvas');glow.width=128;glow.height=128;const gc=glow.getContext('2d'),g=gc.createRadialGradient(64,64,1,64,64,63);
      g.addColorStop(0,'rgba(255,214,155,.65)');g.addColorStop(.5,'rgba(255,204,136,.22)');g.addColorStop(1,'rgba(255,202,120,0)');gc.fillStyle=g;gc.fillRect(0,0,128,128);
      const warm=lighting.pools||lighting.warm||[],pbb=lighting.pbbPools||[],dummy=new THREE.Object3D();
      this.pools=new THREE.InstancedMesh(new THREE.PlaneGeometry(1,1),new THREE.MeshBasicMaterial({map:new THREE.CanvasTexture(glow),transparent:true,depthWrite:false,blending:THREE.AdditiveBlending,opacity:.7,polygonOffset:true,polygonOffsetFactor:-.3,polygonOffsetUnits:-1}),(warm.length+pbb.length)/3);
      for(let i=0;i<warm.length;i+=3){dummy.position.set(warm[i],warm[i+1],.33);dummy.scale.set(150,120,1);dummy.updateMatrix();this.pools.setMatrixAt(i/3,dummy.matrix)}
      for(let i=0;i<pbb.length;i+=3){dummy.position.set(pbb[i],pbb[i+1],pbb[i+2]);dummy.scale.set(30,26,1);dummy.updateMatrix();this.pools.setMatrixAt((warm.length+i)/3,dummy.matrix)}
      this.pools.frustumCulled=false;this.pools.visible=false;this.scene.add(this.pools);
    }
    makeAircraftLights(groups,capacity){
      this.aircraftAnchors=new Map();this.aircraftLightCount=0;
      const point=new THREE.Vector3();
      for(const group of groups){
        const bounds=new THREE.Box3(),left=new THREE.Vector3(0,-Infinity,0),right=new THREE.Vector3(0,Infinity,0);
        // Find real wing tips once from the shared mesh templates, in P2 space.
        for(const part of group.parts){
          const positions=part.mesh.geometry.getAttribute('position');
          for(let i=0;i<positions.count;i++){
            point.fromBufferAttribute(positions,i).applyMatrix4(part.local);bounds.expandByPoint(point);
            if(point.y>left.y)left.copy(point);if(point.y<right.y)right.copy(point);
          }
        }
        if(bounds.isEmpty())continue;
        left.y+=.12;right.y-=.12;left.z+=.12;right.z+=.12;
        const centerY=(bounds.min.y+bounds.max.y)*.5;
        const tail=new THREE.Vector3(bounds.min.x-.12,centerY,Math.max(1.5,bounds.max.z*.58));
        const nose=new THREE.Vector3(bounds.max.x-.6,centerY,Math.max(.85,bounds.min.z+.9));
        this.aircraftAnchors.set(group,[left,right,tail,nose]);
      }
      const geometry=new THREE.BufferGeometry(),positions=new THREE.BufferAttribute(new Float32Array(Math.max(1,capacity)*12),3),colors=new Float32Array(Math.max(1,capacity)*12);
      positions.setUsage(THREE.DynamicDrawUsage);
      const tints=[new THREE.Color('#ff5547'),new THREE.Color('#50ef9f'),new THREE.Color('#fff3dc'),new THREE.Color('#fff8e9')];
      for(let i=0;i<Math.max(1,capacity);i++)for(let j=0;j<4;j++)tints[j].toArray(colors,i*12+j*3);
      geometry.setAttribute('position',positions);geometry.setAttribute('color',new THREE.BufferAttribute(colors,3));geometry.setDrawRange(0,0);
      this.aircraftLights=new THREE.Points(geometry,new THREE.ShaderMaterial({transparent:true,depthWrite:false,vertexColors:true,blending:THREE.AdditiveBlending,
        vertexShader:'varying vec3 vTint;void main(){vTint=color;vec4 mv=modelViewMatrix*vec4(position,1.);gl_PointSize=clamp(2400./max(1.,-mv.z),2.4,7.);gl_Position=projectionMatrix*mv;}',
        fragmentShader:'varying vec3 vTint;void main(){float r=length(gl_PointCoord-.5);if(r>.5)discard;float a=exp(-r*r*72.)+exp(-r*r*12.)*.4;gl_FragColor=vec4(vTint,a);}'
      }));
      this.aircraftLights.frustumCulled=false;this.aircraftLights.visible=false;this.scene.add(this.aircraftLights);
    }
    beginAircraft(){this.aircraftLightCount=0}
    addAircraft(group,x,y,z,heading){
      if(this.mode!=='night')return;
      const anchors=this.aircraftAnchors.get(group);if(!anchors)return;
      const attribute=this.aircraftLights.geometry.getAttribute('position');if((this.aircraftLightCount+1)*4>attribute.count)return;
      const c=Math.cos(heading),s=Math.sin(heading),offset=this.aircraftLightCount*4;
      for(let i=0;i<4;i++){const p=anchors[i];attribute.setXYZ(offset+i,x+p.x*c-p.y*s,y+p.x*s+p.y*c,z+p.z)}
      this.aircraftLightCount++;
    }
    endAircraft(){
      this.aircraftLights.geometry.setDrawRange(0,this.aircraftLightCount*4);
      if(this.mode==='night')this.aircraftLights.geometry.getAttribute('position').needsUpdate=true;
    }
    setMode(mode){
      // Older stored rain/snow states return to the regular daylight view.
      const night=mode==='night';this.mode=night?'night':'clear';document.body.dataset.weather=this.mode;
      this.toolbar.querySelector('button').setAttribute('aria-pressed',String(night));
      this.scene.background=new THREE.Color(night?'#000000':'#f5f5f3');
      this.scene.fog.color.set(night?'#000000':'#f5f5f3');
      this.scene.fog.near=night?5500:8000;this.scene.fog.far=night?16000:20000;
      // Keep the source daylight hue/direction; less fill preserves grey paving
      // and material contrast against the landing page's bright background.
      this.ambient.color.set(night?'#8198bd':'#f4ebe3');this.ambient.intensity=night?.22:.32;
      this.hemi.color.set(night?'#526b94':'#dce6f5');this.hemi.groundColor.set(night?'#17131b':'#6c6f7a');this.hemi.intensity=night?.23:.35;
      this.sun.color.set(night?'#ffc996':'#ffecd8');this.sun.intensity=night?.14:.98;this.sun.castShadow=!night;
      this.renderer.toneMappingExposure=night?1.1:.94;
      for(const base of this.materials){
        const m=base.mat,name=m.name;m.emissive.copy(base.emissive);m.emissiveIntensity=base.emissiveIntensity;m.envMapIntensity=base.env;
        if(night){
          m.envMapIntensity=base.env*.18;
          if(['glass','skylight'].includes(name)){m.emissive.set('#66c4c3').convertSRGBToLinear();m.emissiveIntensity=.65}
          if(name==='bridge-glass'){m.emissive.set('#ffd29b').convertSRGBToLinear();m.emissiveIntensity=.75}
          if(name==='bridge'){m.emissive.set('#dce5ef').convertSRGBToLinear();m.emissiveIntensity=.035}
          if(base.aircraft){m.emissive.copy(m.color).multiplyScalar(.1);m.emissiveIntensity=1}
        }
      }
      this.nightLights.visible=night;this.pools.visible=night;this.aircraftLights.visible=night;
      this.renderer.shadowMap.needsUpdate=true;this.onChange();
    }
    update(){}
    dispose(){this.toolbar.removeEventListener('click',this.handleClick);this.toolbar.remove()}
  }
  window.AirportWeather=AirportWeather;
})();
