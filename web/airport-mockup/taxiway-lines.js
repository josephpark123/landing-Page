/* One GPU-expanded batch keeps real taxiway paint legible at airport scale. */
(() => {
  'use strict';
  class TaxiwayLines {
    constructor({scene,camera,renderer,meta}) {
      Object.assign(this,{scene,camera,renderer});
      this.size=new THREE.Vector2();this.mesh=null;
      const spec=meta.taxiwayCenterlines,taxiValues=spec?.segments||[],leadValues=spec?.leadInSegments||[];
      this.taxiwaySegmentCount=Math.floor(taxiValues.length/6);
      this.leadInSegmentCount=Math.floor(leadValues.length/6);
      this.segmentCount=this.taxiwaySegmentCount+this.leadInSegmentCount;
      const softerDistanceLines=meta.icao==='RPLL';
      this.minimumCssPixels=softerDistanceLines?.9:(spec?.minimumCssPixels||1.1)/1.1;
      this.farMinimumCssPixels=softerDistanceLines?.5:this.minimumCssPixels;
      this.widthM=spec?.widthM||.5;
      if(!this.segmentCount)return;
      const starts=new Float32Array(this.segmentCount*3),ends=new Float32Array(this.segmentCount*3);
      const widths=new Float32Array(this.segmentCount),minimumScales=new Float32Array(this.segmentCount);
      const bounds=new THREE.Box3(),point=new THREE.Vector3();
      for(let i=0;i<this.segmentCount;i++) {
        const isLeadIn=i>=this.taxiwaySegmentCount,index=isLeadIn?i-this.taxiwaySegmentCount:i;
        const values=isLeadIn?leadValues:taxiValues,offset=index*6;
        starts.set(values.slice(offset,offset+3),i*3);ends.set(values.slice(offset+3,offset+6),i*3);
        widths[i]=isLeadIn?(spec.leadInWidthsM?.[index]||.25):this.widthM;
        minimumScales[i]=isLeadIn?(spec.leadInMinimumScale||.8):1;
        bounds.expandByPoint(point.fromArray(starts,i*3));bounds.expandByPoint(point.fromArray(ends,i*3));
      }
      const geometry=new THREE.InstancedBufferGeometry();
      geometry.setAttribute('position',new THREE.Float32BufferAttribute([0,-1,0,1,-1,0,1,1,0,0,1,0],3));
      geometry.setAttribute('instanceStart',new THREE.InstancedBufferAttribute(starts,3));
      geometry.setAttribute('instanceEnd',new THREE.InstancedBufferAttribute(ends,3));
      geometry.setAttribute('instanceWidth',new THREE.InstancedBufferAttribute(widths,1));
      geometry.setAttribute('instanceMinimumScale',new THREE.InstancedBufferAttribute(minimumScales,1));
      geometry.setIndex([0,1,2,0,2,3]);geometry.instanceCount=this.segmentCount;
      geometry.boundingBox=bounds.expandByScalar(32);geometry.boundingSphere=bounds.getBoundingSphere(new THREE.Sphere());
      const uniforms=THREE.UniformsUtils.merge([THREE.UniformsLib.fog,{
        uResolution:{value:new THREE.Vector2(1,1)},uMinPixels:{value:this.minimumCssPixels},
        uFarMinPixels:{value:this.farMinimumCssPixels},
        uDistanceOpacity:{value:new THREE.Vector2(softerDistanceLines?.75:.85,softerDistanceLines?.45:.5)},
        uNear:{value:camera.near},uBrightness:{value:1},
        uColor:{value:new THREE.Color('#d1b05b').convertSRGBToLinear()}
      }]);
      const material=new THREE.ShaderMaterial({
        name:'taxiway-screen-lines',uniforms,transparent:true,depthTest:true,depthWrite:false,
        fog:true,toneMapped:true,side:THREE.DoubleSide,
        polygonOffset:true,polygonOffsetFactor:-1,polygonOffsetUnits:-8,
        vertexShader:`
          attribute vec3 instanceStart;
          attribute vec3 instanceEnd;
          attribute float instanceWidth;
          attribute float instanceMinimumScale;
          uniform vec2 uResolution;
          uniform float uMinPixels;
          uniform float uFarMinPixels;
          uniform vec2 uDistanceOpacity;
          uniform float uNear;
          varying float vDistance;
          varying float vHalfWidth;
          varying float vOpacity;
          #include <fog_pars_vertex>
          void main() {
            vec4 startView=modelViewMatrix*vec4(instanceStart,1.);
            vec4 endView=modelViewMatrix*vec4(instanceEnd,1.);
            float clipNear=-uNear*1.001;
            if(startView.z>clipNear && endView.z>clipNear) {
              vOpacity=0.;vDistance=0.;vHalfWidth=0.;gl_Position=vec4(2.,2.,2.,1.);return;
            }
            // Clip in view space before dividing by W. Segments crossing the
            // near plane cannot explode into airport-wide screen rectangles.
            if(startView.z>clipNear)startView=mix(startView,endView,(clipNear-startView.z)/(endView.z-startView.z));
            if(endView.z>clipNear)endView=mix(endView,startView,(clipNear-endView.z)/(startView.z-endView.z));
            vec4 startClip=projectionMatrix*startView;
            vec4 endClip=projectionMatrix*endView;
            vec2 screenDirection=(endClip.xy/endClip.w-startClip.xy/startClip.w)*uResolution;
            float projectedLength=length(screenDirection);
            vec2 screenNormal=vec2(-screenDirection.y,screenDirection.x)/max(projectedLength,.0001);
            vec4 mvPosition=mix(startView,endView,position.x);
            vec4 centerClip=projectionMatrix*mvPosition;
            vec3 worldDirection=normalize(instanceEnd-instanceStart);
            vec3 sideView=mat3(modelViewMatrix)*vec3(-worldDirection.y,worldDirection.x,0.);
            vec4 physicalEdge=projectionMatrix*(mvPosition+vec4(sideView*instanceWidth*.5,0.));
            vec2 physicalOffset=(physicalEdge.xy/physicalEdge.w-centerClip.xy/centerClip.w)*uResolution*.5;
            float physicalPixels=2.*abs(dot(physicalOffset,screenNormal));
            // Near paint remains the original 0.5 m ground mesh. This batch
            // only supplements it as its projected width becomes subpixel.
            // MNL's compact layout needs a quieter far view. Keep ICN's
            // constant floor while MNL gently approaches 0.55 px at 5 km.
            float distanceBlend=smoothstep(1000.,5000.,-mvPosition.z);
            float minimumPixels=mix(uMinPixels,uFarMinPixels,distanceBlend)*instanceMinimumScale;
            vOpacity=(1.-smoothstep(minimumPixels,minimumPixels*1.35,physicalPixels))*mix(uDistanceOpacity.x,uDistanceOpacity.y,distanceBlend);
            if(projectedLength<.0001)vOpacity=0.;
            vHalfWidth=max(physicalPixels,minimumPixels)*.5;
            float antialiasExtent=vHalfWidth+.75;
            vDistance=position.y*antialiasExtent;
            centerClip.xy+=screenNormal*vDistance*2./uResolution*centerClip.w;
            gl_Position=centerClip;
            #include <fog_vertex>
          }
        `,
        fragmentShader:`
          uniform vec3 uColor;
          uniform float uBrightness;
          varying float vDistance;
          varying float vHalfWidth;
          varying float vOpacity;
          #include <fog_pars_fragment>
          void main() {
            float coverage=1.-smoothstep(vHalfWidth-.5,vHalfWidth+.5,abs(vDistance));
            float alpha=coverage*vOpacity;
            if(alpha<.005)discard;
            gl_FragColor=vec4(uColor*uBrightness,alpha);
            #include <tonemapping_fragment>
            #include <encodings_fragment>
            #include <fog_fragment>
          }
        `
      });
      this.mesh=new THREE.Mesh(geometry,material);this.mesh.name='taxiway-minimum-pixel-lines';this.mesh.renderOrder=20;
      // Constant per-draw uniforms only: no segment projection or buffer upload
      // while orbiting, scrubbing, playing, or changing the cinematic camera.
      this.mesh.onBeforeRender=()=>{
        uniforms.uNear.value=this.camera.near;
        uniforms.uBrightness.value=document.body.dataset.weather==='night'?.28:1;
      };
      scene.add(this.mesh);this.resize();
    }
    resize() {
      if(!this.mesh)return;
      this.renderer.getDrawingBufferSize(this.size);
      this.mesh.material.uniforms.uResolution.value.copy(this.size);
      this.mesh.material.uniforms.uMinPixels.value=this.minimumCssPixels*this.renderer.getPixelRatio();
      this.mesh.material.uniforms.uFarMinPixels.value=this.farMinimumCssPixels*this.renderer.getPixelRatio();
    }
    dispose() {
      if(!this.mesh)return;
      this.scene.remove(this.mesh);this.mesh.geometry.dispose();this.mesh.material.dispose();this.mesh=null;
    }
  }
  window.TaxiwayLines=TaxiwayLines;
})();
