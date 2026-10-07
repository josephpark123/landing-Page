/* Prebuilt airport runtime. Three r128, Z-up, metres, P2 aircraft pivots. */
(() => {
  'use strict';
  const assetBase=new URL('.',document.currentScript.src);
  const presetCodes={RKSI:'RKSI',ICN:'RKSI',RPLL:'RPLL',MNL:'RPLL',VTBS:'VTBS',BKK:'VTBS',RJAA:'RJAA',NRT:'RJAA',VVTS:'VVTS',SGN:'VVTS',LOWW:'LOWW',VIE:'LOWW'};
  const requestedAirport=presetCodes[(new URLSearchParams(location.search).get('airport')||'RKSI').trim().toUpperCase()]||'RKSI';
  let modelBase=assetBase;
  const $=id=>document.getElementById(id),host=$('viewport');
  const reduced=matchMedia('(prefers-reduced-motion: reduce)').matches;
  const mobile=/KAKAOTALK/i.test(navigator.userAgent)||matchMedia('(pointer: coarse)').matches||(navigator.maxTouchPoints>0&&Math.min(screen.width,screen.height)<=1024);
  const scene=new THREE.Scene();scene.background=new THREE.Color('#f5f5f3');
  scene.fog=new THREE.Fog('#f5f5f3',8000,20000);
  let renderer;
  try{renderer=new THREE.WebGLRenderer({antialias:true,powerPreference:'high-performance'})}
  catch(error){showLoadError('This device could not start the 3D view. Please reload to try again.');return}
  renderer.setPixelRatio(Math.min(devicePixelRatio,mobile?1.1:1.4));renderer.outputEncoding=THREE.sRGBEncoding;
  renderer.toneMapping=THREE.ACESFilmicToneMapping;renderer.toneMappingExposure=1.22;
  renderer.shadowMap.enabled=true;renderer.shadowMap.type=THREE.PCFSoftShadowMap;
  renderer.shadowMap.autoUpdate=false;host.appendChild(renderer.domElement);
  const camera=new THREE.PerspectiveCamera(36,1,2,40000);camera.up.set(0,0,1);
  const controls=new THREE.OrbitControls(camera,renderer.domElement);
  controls.enableDamping=true;controls.dampingFactor=.07;controls.minDistance=65;controls.maxDistance=14000;
  controls.maxPolarAngle=Math.PI*.485;controls.panSpeed=.7;controls.zoomSpeed=.8;controls.rotateSpeed=.55;
  controls.screenSpacePanning=false;
  // Match 260903's balanced airport_day palette with the landing page's white sky.
  const sunOffset=new THREE.Vector3(2500,1400,4200);
  const ambient=new THREE.AmbientLight('#f4ebe3',.52);scene.add(ambient);
  const hemi=new THREE.HemisphereLight('#dce6f5','#6c6f7a',.46);hemi.position.set(0,0,1);scene.add(hemi);
  const sun=new THREE.DirectionalLight('#ffecd8',.98);sun.position.copy(sunOffset);sun.castShadow=true;
  sun.shadow.mapSize.set(mobile?1024:2048,mobile?1024:2048);sun.shadow.camera.near=100;sun.shadow.camera.far=10000;
  sun.shadow.bias=-.000025;sun.shadow.normalBias=.32;sun.shadow.radius=2.5;
  scene.add(sun,sun.target);
  // Bake one Z-up daylight environment at startup. Its broad horizon and small
  // warm sun reflection ground the materials without live reflection passes.
  const envScene=new THREE.Scene();
  const skyMaterial=new THREE.ShaderMaterial({side:THREE.BackSide,uniforms:{uSun:{value:sunOffset.clone().normalize()}},
    vertexShader:'varying vec3 vDirection;void main(){vDirection=position;gl_Position=projectionMatrix*modelViewMatrix*vec4(position,1.);}',
    fragmentShader:'uniform vec3 uSun;varying vec3 vDirection;void main(){vec3 d=normalize(vDirection);float h=smoothstep(-.03,.75,d.z);vec3 sky=mix(vec3(.84,.90,.94),vec3(.32,.52,.79),h);sky=mix(vec3(.24,.27,.22),sky,smoothstep(-.12,.03,d.z));float sun=max(dot(d,uSun),0.);sky+=vec3(1.,.82,.58)*(pow(sun,384.)*7.+pow(sun,12.)*.20);gl_FragColor=vec4(sky,1.);\n#include <encodings_fragment>\n}'
  });
  const skyDome=new THREE.Mesh(new THREE.SphereGeometry(30,32,16),skyMaterial);envScene.add(skyDome);
  const pmrem=new THREE.PMREMGenerator(renderer);const env=pmrem.fromScene(envScene,.035);scene.environment=env.texture;pmrem.dispose();skyDome.geometry.dispose();skyMaterial.dispose();
  const floor=new THREE.Mesh(new THREE.PlaneGeometry(150000,150000),new THREE.ShadowMaterial({opacity:.12}));floor.position.z=-12.3;floor.receiveShadow=true;scene.add(floor);
  const dummy=new THREE.Object3D(),combinedMatrix=new THREE.Matrix4();
  const cameraPoint=new THREE.Vector3(),shadowTarget=new THREE.Vector3(Infinity,Infinity,0);let shadowRange=0;
  const frustum=new THREE.Frustum(),projection=new THREE.Matrix4(),aircraftBounds=new THREE.Sphere(new THREE.Vector3(),65);
  let meta,data,time=0,playing=!reduced,speed=30,cinematic=!reduced,tour=0,raf=0,last=performance.now(),ready=false,dirty=true,disposed=false;
  let playbackStart=0,playbackEnd=1,loopReplay=false;
  const loadController=new AbortController();
  let decoder,modelRoot,switching=false,finalSnapshot=null;
  let lastUI=0,visibleCount=0,drawnAircraft=0,renderedFrames=0,weatherEffect,taxiwayLines;
  const aircraftGroups=[],frameTimes=[];
  const shadowCanvas=document.createElement('canvas');shadowCanvas.width=128;shadowCanvas.height=128;
  const ctx=shadowCanvas.getContext('2d');const gradient=ctx.createRadialGradient(64,64,1,64,64,62);gradient.addColorStop(0,'rgba(34,43,32,.62)');gradient.addColorStop(.4,'rgba(34,43,32,.30)');gradient.addColorStop(1,'rgba(34,43,32,0)');ctx.fillStyle=gradient;ctx.fillRect(0,0,128,128);
  const shadowTexture=new THREE.CanvasTexture(shadowCanvas);
  let aircraftShadow;
  const poses={
    overview:{position:[-5600,-6500,6600],target:[-50,350,0]},
    terminal:{position:[-50,-260,530],target:[-650,870,10]},
    airside:{position:[-840,-200,72],target:[-680,280,9]}
  };
  let tourPositions=new THREE.CatmullRomCurve3([
    new THREE.Vector3(-2100,-2700,1950),new THREE.Vector3(-50,-260,530),
    new THREE.Vector3(-420,2020,410),new THREE.Vector3(-2020,1020,600),
    new THREE.Vector3(-2100,-2700,1950)
  ],false,'catmullrom',.25);
  const tourTarget=new THREE.Vector3(-690,820,5);
  function setPose(name){
    if(disposed)return;
    cinematic=false;$('cinematic').setAttribute('aria-pressed','false');document.body.classList.add('exploring');
    document.querySelectorAll('.view-tools button').forEach(b=>b.classList.toggle('active',b.id===name));
    const p=poses[name];camera.position.fromArray(p.position);controls.target.fromArray(p.target);controls.update();dirty=true;
  }
  function updateCinematic(){
    tourPositions.getPoint((tour%90)/90,cameraPoint);camera.position.copy(cameraPoint);
    controls.target.copy(tourTarget);controls.update();
    document.body.classList.toggle('tour-running',tour>7);
  }
  controls.addEventListener('start',()=>{
    cinematic=false;document.body.classList.add('exploring');$('cinematic').setAttribute('aria-pressed','false');
    document.querySelectorAll('.view-tools button').forEach(b=>b.classList.remove('active'));dirty=true;
  });
  controls.addEventListener('change',()=>{dirty=true});
  for(const name of ['overview','terminal','airside'])$(name).addEventListener('click',()=>setPose(name));
  $('cinematic').addEventListener('click',()=>{
    cinematic=!cinematic;$('cinematic').setAttribute('aria-pressed',String(cinematic));
    document.body.classList.toggle('exploring',!cinematic);
    document.querySelectorAll('.view-tools button').forEach(b=>b.classList.toggle('active',b.id==='cinematic'&&cinematic));dirty=true;
  });
  function setPlaying(value){if(disposed)return;if(value&&meta&&time>=playbackEnd-.1)time=playbackStart;playing=value&&(!meta||meta.tracks.length>0);$('play').setAttribute('aria-label',playing?'Pause replay':'Play replay');$('play-icon').innerHTML=playing?'<path d="M7 5h4v14H7zm6 0h4v14h-4z"/>':'<path d="m8 5 11 7-11 7V5Z"/>';dirty=true;}
  $('play').addEventListener('click',()=>setPlaying(!playing));
  $('timeline').addEventListener('input',()=>{if(!ready||disposed)return;time=Number($('timeline').value);updateAircraft();updateUI();dirty=true});
  $('speed').addEventListener('click',()=>{const speeds=[1,10,30,60,120];speed=speeds[(speeds.indexOf(speed)+1)%speeds.length];$('speed').textContent=speed+'×';$('speed').setAttribute('aria-label','Playback speed: '+speed+' times')});
  function onKey(e){if(e.code==='Space'&&!['INPUT','BUTTON','A','SELECT','OPTION'].includes(e.target.tagName)){e.preventDefault();if(ready)setPlaying(!playing)}}
  document.addEventListener('keydown',onKey);
  const formatter=new Intl.DateTimeFormat('en-GB',{hour:'2-digit',minute:'2-digit',second:'2-digit',timeZone:'UTC'});
  function clock(sec){return formatter.format(new Date(Math.round(sec)*1000))}
  function updateUI(){
    $('clock').textContent=clock(meta.start+time);$('timeline').value=time;
    $('timeline').style.setProperty('--progress',((time-playbackStart)/(playbackEnd-playbackStart)*100)+'%');
    $('timeline').setAttribute('aria-valuetext',clock(meta.start+time));$('visible-count').textContent=visibleCount;
  }
  function indexAt(track,t){
    let lo=0,hi=track.count-1;const offset=track.offset;
    while(lo+1<hi){const mid=(lo+hi)>>>1;if(data[offset+mid*5]<=t)lo=mid;else hi=mid}
    return lo;
  }
  function updateAircraft(){
    visibleCount=0;drawnAircraft=0;let shadowIndex=0;
    if(weatherEffect?.beginAircraft)weatherEffect.beginAircraft();
    camera.updateMatrixWorld();projection.multiplyMatrices(camera.projectionMatrix,camera.matrixWorldInverse);frustum.setFromProjectionMatrix(projection);
    for(const group of aircraftGroups){
      let instanceIndex=0;
      for(let i=0;i<group.tracks.length;i++){
        const tr=group.tracks[i];const idx=indexAt(tr,time);const off=tr.offset+idx*5,next=Math.min(off+5,tr.offset+(tr.count-1)*5);
        const dt=data[next]-data[off];const a=dt>0?Math.max(0,Math.min(1,(time-data[off])/dt)):0;
        const x=data[off+1]+(data[next+1]-data[off+1])*a,y=data[off+2]+(data[next+2]-data[off+2])*a;
        const z=data[off+3]+(data[next+3]-data[off+3])*a,h=data[off+4]+(data[next+4]-data[off+4])*a;
        const b=meta.siteBounds,active=time>=tr.start&&time<=tr.end&&x>b[0]-2000&&x<b[2]+2000&&y>b[1]-2000&&y<b[3]+2000;
        if(!active)continue;
        visibleCount++;aircraftBounds.center.set(x,y,z);
        if(!frustum.intersectsSphere(aircraftBounds))continue;
        if(weatherEffect?.addAircraft)weatherEffect.addAircraft(group,x,y,Math.max(0,z)+.32,h);
        dummy.position.set(x,y,Math.max(0,z)+.32);dummy.rotation.set(0,0,h);dummy.scale.setScalar(1);dummy.updateMatrix();
        for(const part of group.parts){combinedMatrix.multiplyMatrices(dummy.matrix,part.local);part.mesh.setMatrixAt(instanceIndex,combinedMatrix)}
        instanceIndex++;drawnAircraft++;
        if(z<35){dummy.position.set(x,y,.36);dummy.scale.set(group.length*1.07,group.span*.65,1);dummy.updateMatrix();aircraftShadow.setMatrixAt(shadowIndex++,dummy.matrix)}
      }
      for(const part of group.parts){part.mesh.count=instanceIndex;part.mesh.instanceMatrix.needsUpdate=true}
    }
    aircraftShadow.count=shadowIndex;aircraftShadow.instanceMatrix.needsUpdate=true;
    if(weatherEffect?.endAircraft)weatherEffect.endAircraft();
  }
  function prepareAircraft(root,type){
    root.updateMatrixWorld(true);const tracks=meta.tracks.filter(t=>t.type===type),parts=[];
    const bbox=new THREE.Box3().setFromObject(root),size=bbox.getSize(new THREE.Vector3());
    root.traverse(node=>{
      if(!node.isMesh)return;
      const mesh=new THREE.InstancedMesh(node.geometry,node.material,tracks.length);
      mesh.instanceMatrix.setUsage(THREE.DynamicDrawUsage);mesh.receiveShadow=true;
      // Aircraft move far beyond the source mesh bounds. These 33 small batches
      // are explicitly culled per instance above, instead of using stale bounds.
      mesh.frustumCulled=false;scene.add(mesh);
      parts.push({mesh,local:node.matrixWorld.clone()});
      if(node.material){node.material.envMapIntensity=.65;node.material.side=THREE.DoubleSide}
    });
    aircraftGroups.push({type,tracks,parts,length:size.x,span:size.y,bounds:{min:bbox.min.toArray(),max:bbox.max.toArray()}});root.removeFromParent?root.removeFromParent():root.parent.remove(root);
  }
  function shadowCamera(){
    // Tighter close-view coverage resolves jet bridges and building contacts;
    // coarse range steps preserve the existing cached, static shadow pass.
    const range=Math.max(900,Math.min(1800,Math.ceil(camera.position.distanceTo(controls.target)*.8/300)*300));
    if(shadowTarget.distanceTo(controls.target)<180&&range===shadowRange)return;
    shadowRange=range;
    shadowTarget.copy(controls.target);sun.target.position.copy(shadowTarget);
    sun.position.copy(shadowTarget).add(sunOffset);
    Object.assign(sun.shadow.camera,{left:-range,right:range,top:range,bottom:-range});sun.shadow.camera.updateProjectionMatrix();renderer.shadowMap.needsUpdate=true;
  }
  function resize(){if(disposed)return;const w=host.clientWidth,h=host.clientHeight;if(!w||!h)return;renderer.setSize(w,h);camera.aspect=w/h;camera.updateProjectionMatrix();if(taxiwayLines)taxiwayLines.resize();dirty=true}
  const resizeObserver=new ResizeObserver(resize);resizeObserver.observe(host);
  let loadedAt=0,loadBegan=0;
  async function load(){
    loadBegan=performance.now();
    let assetVersions={};
    if(window.airportSelectionReady){const selection=await window.airportSelectionReady;if(selection?.assetBase)modelBase=new URL(selection.assetBase,location.origin);assetVersions=selection?.assetVersions||{}}
    else if(requestedAirport!=='RKSI')modelBase=new URL('/web/airport-mockup/airports/'+requestedAirport+'/',location.origin);
    // Each content revision has its own browser cache entry. Unversioned
    // fallback URLs still revalidate, so an older bootstrap cannot freeze data.
    const assetUrl=name=>{const url=new URL(name,modelBase);if(assetVersions[name])url.searchParams.set('v',assetVersions[name]);return url};
    if(disposed)return;
    const requests=await Promise.all([fetch(assetUrl('scene.json'),{signal:loadController.signal}).then(r=>{if(!r.ok)throw Error('This airport model is unavailable. Please reload and try again.');return r.json()}),fetch(assetUrl('replay.bin'),{signal:loadController.signal}).then(r=>{if(!r.ok)throw Error('Replay unavailable');return r.arrayBuffer()})]);
    if(disposed)return;
    meta=requests[0];data=new Float32Array(requests[1]);speed=meta.speed;
    // Window endpoints are absolute recording seconds. Keep the original time
    // anchor so trimmed Float32 samples retain exactly the same interpolation.
    const replayWindow=meta.playbackWindow||(meta.icao==='RKSI'?{start:43200,end:44400,loop:true}:null);
    const hasWindow=replayWindow&&Number.isFinite(replayWindow.start)&&Number.isFinite(replayWindow.end)&&replayWindow.end>replayWindow.start;
    playbackStart=hasWindow?Math.max(0,replayWindow.start-meta.start):0;
    playbackEnd=hasWindow?Math.min(meta.duration,replayWindow.end-meta.start):meta.duration;
    if(playbackEnd<=playbackStart){playbackStart=0;playbackEnd=meta.duration;loopReplay=false}
    else loopReplay=Boolean(hasWindow&&replayWindow.loop);
    time=hasWindow?playbackStart:Math.min(playbackEnd,meta.initialTime);
    if(meta.camera){Object.assign(poses,meta.camera.poses);tourTarget.fromArray(meta.camera.tourTarget);tourPositions=new THREE.CatmullRomCurve3(meta.camera.tourPositions.map(p=>new THREE.Vector3().fromArray(p)),false,'catmullrom',.25)}
    if(window.airportSelector)window.airportSelector.setCurrent(meta.icao,meta.airport);
    document.querySelector('.scene-heading .eyebrow').textContent=meta.airport.toUpperCase();
    document.querySelector('.scene-footer span:first-child').textContent=meta.scenario;
    $('experience').setAttribute('aria-label','Interactive '+meta.airport+' scene');
    document.body.classList.toggle('no-replay',meta.tracks.length===0);
    if(!meta.tracks.length){document.querySelector('.timeline-labels span').textContent='EXPLORE THIS AIRPORT';document.querySelector('.traffic-count span').textContent='saved movements';$('clock').hidden=true}
    $('timeline').min=playbackStart;$('timeline').max=playbackEnd;$('start-time').textContent=clock(meta.start+playbackStart).slice(0,5);$('end-time').textContent=clock(meta.start+playbackEnd).slice(0,5);
    const loader=new THREE.GLTFLoader();
    if(THREE.DRACOLoader){decoder=new THREE.DRACOLoader();decoder.setDecoderPath(new URL('vendor/draco/',assetBase).href);decoder.setWorkerLimit(mobile?1:2);loader.setDRACOLoader(decoder)}
    // r128 GLTFLoader.load does not expose its request. Fetch explicitly so
    // switching during download can abort it before the next model starts.
    const response=await fetch(assetUrl('airport-scene.glb'),{signal:loadController.signal});
    if(!response.ok)throw Error('Airport model unavailable');
    let payload=await response.arrayBuffer();
    if(disposed)return;
    $('loading-detail').textContent='Preparing the airport';$('loading-progress').style.width='65%';
    const gltf=await new Promise((resolve,reject)=>{
      const signal=loadController.signal,aborted=()=>reject(new DOMException('Aborted','AbortError'));
      signal.addEventListener('abort',aborted,{once:true});
      loader.parse(payload,modelBase.href,value=>{signal.removeEventListener('abort',aborted);if(disposed){releaseObjects(value.scene);return}resolve(value)},error=>{signal.removeEventListener('abort',aborted);reject(error)});
    });
    payload=null;
    if(decoder){decoder.dispose();decoder=null}
    if(disposed){releaseObjects(gltf.scene);return}
    const root=gltf.scene;modelRoot=root;
    const templates=root.children.filter(child=>child.userData.aircraftType);
    for(const template of templates)prepareAircraft(template,template.userData.aircraftType);
    if(aircraftGroups.length!==Object.keys(meta.models).length)throw new Error('Aircraft templates missing');
    root.traverse(node=>{
      if(!node.isMesh)return;
      const name=node.material.name;
      node.castShadow=['glass','mullion','roof','tower','building','building-roof','bridge','bridge-glass','plinth','road-curb','road-deck'].includes(name);
      node.receiveShadow=true;node.material.envMapIntensity=['glass','skylight','bridge-glass'].includes(name)?.24:.2;
      if(['taxiway','runway'].includes(name)){
        if(!node.material.userData?.sourcePavementTone)node.material.color.multiplyScalar(.65);
        node.material.roughness=node.material.roughnessMap?1:name==='taxiway'?.84:.92;
        node.material.metalness=0;node.material.envMapIntensity=name==='taxiway'?.14:.08;
        if(node.material.normalScale)node.material.normalScale.setScalar(.55);
      }
      if(['road','road-deck'].includes(name)){if(!node.material.map)node.material.color.set('#bcc3c7').convertSRGBToLinear();node.material.roughness=node.material.roughnessMap?1:.84;node.material.metalness=0;node.material.envMapIntensity=.12}
      if(name==='roof'){node.material.color.set('#aab8c3').convertSRGBToLinear();node.material.roughness=.9;node.material.metalness=.01;node.material.envMapIntensity=.14}
      if(name==='apron'){if(!node.material.userData?.sourcePavementTone)node.material.color.multiplyScalar(.82);node.material.roughness=node.material.roughnessMap?1:.84;node.material.metalness=0;node.material.envMapIntensity=.14}
      if(name==='grass'){node.material.roughness=1;node.material.metalness=0;node.material.envMapIntensity=.12}
      const surfaceTone={grass:'#6e824e',runway:'#43494c',taxiway:'#54595c',apron:'#757a7d',parking:'#83888a',road:'#8c9193','road-deck':'#8c9193'}[name];
      if(surfaceTone){
        // Keep the source microtexture/normal/roughness but remove the brown
        // photographic cast. Palette and texture contrast remain independent.
        const mat=node.material;mat.color.set(surfaceTone).convertSRGBToLinear();
        mat.onBeforeCompile=shader=>{shader.fragmentShader=shader.fragmentShader.replace('#include <map_fragment>',`#ifdef USE_MAP
          vec4 surfaceTexel = mapTexelToLinear(texture2D(map, vUv));
          float surfaceGrain = dot(surfaceTexel.rgb, vec3(.2126,.7152,.0722));
          diffuseColor.rgb *= mix(.78, 1.18, clamp(surfaceGrain * 2.4, 0., 1.));
          diffuseColor.a *= surfaceTexel.a;
        #endif`)};
        mat.customProgramCacheKey=()=> 'source-neutral-surface-v3';
      }
      const fade={'road-marking':[260,900],'yellow-marking':[600,2100],'white-marking':[2800,7000],'roof-seam':[350,1300]}[name];
      if(fade){
        // Conventional depth keeps MSAA and slope-aware decal bias compatible.
        // Distant subpixel paint fades smoothly instead of flashing on/off.
        const mat=node.material;mat.polygonOffset=true;mat.polygonOffsetFactor=-1;mat.polygonOffsetUnits=-4;
        mat.transparent=true;mat.depthWrite=false;mat.envMapIntensity=0;mat.metalness=0;mat.roughness=.95;
        mat.onBeforeCompile=shader=>{shader.fragmentShader=shader.fragmentShader.replace('#include <dithering_fragment>',`gl_FragColor.a *= 1.0 - smoothstep(${fade[0]}.0, ${fade[1]}.0, length(vViewPosition));\n#include <dithering_fragment>`)};
        mat.customProgramCacheKey=()=>name+'-distance-paint-v1';
      }
      if(['glass','bridge-glass','mullion'].includes(name))node.material.side=THREE.DoubleSide;
    });
    scene.add(root);
    if(window.TaxiwayLines)taxiwayLines=new TaxiwayLines({scene,camera,renderer,meta});
    aircraftShadow=new THREE.InstancedMesh(new THREE.PlaneGeometry(1,1),new THREE.MeshBasicMaterial({map:shadowTexture,transparent:true,depthWrite:false,opacity:.9}),Math.max(1,meta.tracks.length));aircraftShadow.frustumCulled=false;scene.add(aircraftShadow);
    weatherEffect=new AirportWeather({scene,renderer,camera,controls,ambient,hemi,sun,meta,reduced,aircraftGroups,onChange:()=>{dirty=true}});
    let restored=false;
    try {
      const historyReturn=performance.getEntriesByType('navigation')[0]?.type==='back_forward';
      if(sessionStorage.getItem('restore-airport-view')==='true'||historyReturn){
        sessionStorage.removeItem('restore-airport-view');
        const state=JSON.parse(sessionStorage.getItem('airport-view'));
        if(state?.ready&&(state.icao||'RKSI')===meta.icao&&state.camera?.length===3&&state.target?.length===3){
          time=Math.max(playbackStart,Math.min(playbackEnd,state.time));speed=state.speed||30;tour=state.tour||0;
          playing=state.playing&&!reduced;cinematic=state.cinematic&&!reduced;
          camera.position.fromArray(state.camera);controls.target.fromArray(state.target);controls.update();
          document.body.classList.toggle('exploring',!cinematic);
          document.querySelectorAll('.view-tools button').forEach(b=>b.classList.toggle('active',b.id===state.view));
          $('speed').textContent=speed+'×';$('speed').setAttribute('aria-label','Playback speed: '+speed+' times');
          weatherEffect.setMode(state.weather);restored=true;
        }
      }
    } catch (_) {}
    if(!restored||cinematic)updateCinematic();resize();updateClipping();updateAircraft();shadowCamera();weatherEffect.update(0,false);renderer.compile(scene,camera);renderer.render(scene,camera);
    ready=true;loadedAt=performance.now();$('loading-progress').style.width='100%';$('loader').classList.add('loaded');$('loader').setAttribute('aria-hidden','true');
    for(const id of ['play','timeline','speed'])$(id).disabled=meta.tracks.length===0;
    $('cinematic').setAttribute('aria-pressed',String(cinematic));$('cinematic').classList.toggle('active',cinematic);
    setPlaying(playing);updateUI();
    Object.assign(window.airportMockup,{
      sampleAircraft:(id)=>{const tr=meta.tracks.find(t=>t.id===id);if(!tr)return null;const off=tr.offset+indexAt(tr,time)*5,next=Math.min(off+5,tr.offset+(tr.count-1)*5),dt=data[next]-data[off],a=dt>0?Math.max(0,Math.min(1,(time-data[off])/dt)):0;return [1,2,3,4].map(k=>data[off+k]+(data[next+k]-data[off+k])*a)},
      inspectTour:(seconds)=>{setPlaying(false);tour=seconds;cinematic=true;updateCinematic();dirty=true},
      inspectCamera:(position,target)=>{if(![position,target].every(v=>Array.isArray(v)&&v.length===3&&v.every(Number.isFinite)))return;setPlaying(false);cinematic=false;camera.position.fromArray(position);controls.target.fromArray(target);controls.update();dirty=true},
    });
    window.dispatchEvent(new Event('airport-scene-ready'));
  }
  function updateClipping(){const distance=camera.position.distanceTo(controls.target);const near=Math.max(2,distance*.035),far=Math.max(12000,distance+12000);if(Math.abs(camera.near-near)>.1||Math.abs(camera.far-far)>10){camera.near=near;camera.far=far;camera.updateProjectionMatrix()}}
  function frame(now){
    if(disposed)return;raf=requestAnimationFrame(frame);
    const interval=now-last,delta=Math.min(interval/1000,.1);last=now;
    if(!ready||document.hidden)return;
    if(playing){time+=delta*speed;if(time>=playbackEnd){if(loopReplay)time=playbackStart+(time-playbackStart)%(playbackEnd-playbackStart);else{time=playbackEnd;setPlaying(false)}}dirty=true}
    if(cinematic&&(playing||!meta.tracks.length)){tour+=delta;updateCinematic();dirty=true}else controls.update();
    weatherEffect.update(delta,playing);
    if(now-lastUI>120){updateUI();lastUI=now}
    if(dirty){updateClipping();updateAircraft();shadowCamera();renderer.render(scene,camera);renderedFrames++;dirty=false;if(playing&&now-loadedAt>2500){frameTimes.push(interval);if(frameTimes.length>300)frameTimes.shift()}}
  }
  function getSnapshot(){
    if(disposed)return {...finalSnapshot,ready:false,disposed:true,playing:false,geometries:0,textures:0,rafActive:false};
    return {ready,disposed:false,icao:meta?.icao||requestedAirport,airport:meta?.airport,hasReplay:!!meta?.tracks.length,playing,cinematic,tour,speed,view:document.querySelector('.view-tools button.active')?.id,weather:weatherEffect?.mode||'clear',time,absoluteTime:(meta?.start||0)+time,visibleCount,drawnAircraft,renderedFrames,firstUsableMs:loadedAt?Math.round(loadedAt-loadBegan):0,calls:renderer.info.render.calls,triangles:renderer.info.render.triangles,geometries:renderer.info.memory.geometries,textures:renderer.info.memory.textures,pixelRatio:renderer.getPixelRatio(),shadowMapSize:sun.shadow.mapSize.x,decoderWorkers:mobile?1:2,mobile,rafActive:!!raf,frames:frameTimes.slice(),camera:camera.position.toArray(),target:controls.target.toArray()};
  }
  function releaseObjects(...roots){
    const geometries=new Set(),materials=new Set(),textures=new Set(),images=new Set();
    for(const root of roots)root?.traverse(o=>{
      if(o.geometry)geometries.add(o.geometry);
      for(const m of o.material?Array.isArray(o.material)?o.material:[o.material]:[]){
        materials.add(m);for(const value of Object.values(m))if(value?.isTexture)textures.add(value);
        for(const uniform of Object.values(m.uniforms||{}))if(uniform.value?.isTexture)textures.add(uniform.value);
      }
    });
    textures.forEach(texture=>{for(const source of Array.isArray(texture.image)?texture.image:[texture.image])if(source?.close)images.add(source);texture.dispose()});
    geometries.forEach(g=>g.dispose());materials.forEach(m=>m.dispose());images.forEach(img=>img.close());
  }
  function dispose(){
    if(disposed)return;
    finalSnapshot=getSnapshot();disposed=true;ready=false;playing=false;
    loadController.abort();if(decoder){decoder.dispose();decoder=null}
    cancelAnimationFrame(raf);raf=0;resizeObserver.disconnect();controls.dispose();
    document.removeEventListener('keydown',onKey);renderer.domElement.removeEventListener('webglcontextlost',onContextLost);
    if(weatherEffect)weatherEffect.dispose();if(taxiwayLines)taxiwayLines.dispose();
    releaseObjects(scene,modelRoot);env.dispose();shadowTexture.dispose();
    // Light shadow targets are owned separately from mesh textures in r128.
    for(const light of [sun]){light.shadow.map?.dispose();light.shadow.mapPass?.dispose();light.shadow.map=null;light.shadow.mapPass=null}
    scene.environment=null;scene.clear();modelRoot=null;aircraftGroups.length=0;
    weatherEffect=null;taxiwayLines=null;aircraftShadow=null;meta=null;data=null;
    renderer.renderLists.dispose();renderer.dispose();renderer.forceContextLoss();
    renderer.domElement.width=1;renderer.domElement.height=1;renderer.domElement.remove();
    window.dispatchEvent(new Event('airport-scene-disposed'));
  }
  function prepareNavigation({preserveState=true}={}){
    if(preserveState){const state=disposed?finalSnapshot:getSnapshot();if(state?.ready)try{sessionStorage.setItem('airport-view',JSON.stringify(state))}catch(_){}}
    dispose();
  }
  async function loadAirport(value){
    const code=presetCodes[String(value).trim().toUpperCase()];
    if(!code)throw Error('Unknown airport');
    if(switching)return;
    if(code===requestedAirport&&!disposed)return;
    switching=true;window.FlexaPageTransitions?.prepareAirportChange();
    prepareNavigation({preserveState:false});
    // Yield the released graphics context before constructing another page.
    await new Promise(resolve=>setTimeout(resolve,0));
    try{location.assign(code==='RKSI'?'/':'/?airport='+code)}
    catch(error){switching=false;showLoadError('Could not open that airport. Please reload and try again.');throw error}
  }
  function showLoadError(message){
    const panel=$('loader');panel.classList.remove('loaded');panel.setAttribute('aria-hidden','false');
    $('loading-detail').textContent=message;panel.querySelector('strong').textContent='Let’s try that again';panel.querySelector('.loading-orbit').style.animation='none';
    if(!panel.querySelector('.scene-retry')){const retry=document.createElement('button');retry.type='button';retry.className='scene-retry';retry.textContent='Reload 3D view';retry.style.cssText='margin:18px;padding:12px 20px;border:0;border-radius:22px;background:#0071e3;color:white;font:inherit;cursor:pointer;pointer-events:auto';retry.addEventListener('click',()=>location.reload());panel.appendChild(retry)}
    window.dispatchEvent(new Event('airport-scene-error'));
  }
  function onContextLost(event){if(disposed)return;event.preventDefault();prepareNavigation();showLoadError('The 3D view paused to free memory. Reload to continue.')}
  renderer.domElement.addEventListener('webglcontextlost',onContextLost);
  // This API exists during fetch/decode as well as after the first frame.
  window.airportMockup={getSnapshot,loadAirport,prepareNavigation,dispose};
  window.addEventListener('pagehide',event=>{if(mobile||!event.persisted)prepareNavigation({preserveState:!switching})});
  window.addEventListener('pageshow',event=>{
    if(!event.persisted)return;
    if(disposed){
      try{if(finalSnapshot?.ready){sessionStorage.setItem('airport-view',JSON.stringify(finalSnapshot));sessionStorage.setItem('restore-airport-view','true')}}catch(_){}
      location.reload();
    }else{try{sessionStorage.removeItem('restore-airport-view')}catch(_){}}
  });
  document.addEventListener('visibilitychange',()=>{if(!disposed){last=performance.now();dirty=true}});
  load().catch(error=>{if(disposed||error.name==='AbortError')return;console.error(error);dispose();showLoadError('The scene could not load. Please reload to try again.')});
  raf=requestAnimationFrame(frame);
})();
