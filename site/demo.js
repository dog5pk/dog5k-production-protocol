const scenes = [
  {
    label:'THE REQUEST',
    html:`<div class="scene-inner"><p class="eyebrow">A real production task</p><h1>“Finish the DPP whitepaper PDF.”</h1><p class="lead">The generator ran. A PDF existed. The website linked to it. That looked like completion.</p><div class="principles"><span class="pill">Finish the Work</span><span class="pill">Truth Over Confidence</span><span class="pill">Build for Inspection</span></div></div>`
  },
  {
    label:'THE FALSE FINISH',
    html:`<div class="scene-inner"><p class="eyebrow">Generated ≠ verified</p><h2>The first status was too optimistic.</h2><div class="split"><div class="card"><div class="status warn"><span class="dot"></span>Pipeline complete</div><p class="lead">The PDF generator worked and publication automation existed.</p></div><div class="card"><div class="status bad"><span class="dot"></span>Not inspected</div><p class="lead">No one had actually rendered every page and checked the artifact.</p></div></div><p class="lead">Under DPP, “should work” is not the same as “passed inspection.”</p></div>`
  },
  {
    label:'INSPECTION',
    html:`<div class="scene-inner"><p class="eyebrow">Principle VII · Think Before Producing</p><h2>Render it. Inspect it. Believe the artifact.</h2><div class="split"><div class="mock-page"><b>THE DOG5PK PRODUCTION PROTOCOL</b><p>Publication-ready whitepaper...</p><div class="dup"><b>DEFECT:</b><br>Whitepaper Version: 1.0<br>Protocol Baseline: DPP v1.3<br>Author: Dog5pk<br><br>Metadata was duplicated in the body after already appearing on the cover.</div></div><div><p class="lead">Visual QA exposed a real layout defect that generation alone did not reveal.</p><div class="principles"><span class="pill">Known Defects Must Be Corrected</span><span class="pill">Reality Wins</span></div></div></div></div>`
  },
  {
    label:'CORRECTION',
    html:`<div class="scene-inner"><p class="eyebrow">Principle II · Known Defects Must Be Corrected</p><h2>Fix the defect before calling it finished.</h2><div class="checklist"><div class="check"><span class="mark">✓</span><div><strong>Duplicate publication block removed</strong><span>Canonical metadata remains on the cover where it belongs.</span></div></div><div class="check"><span class="mark">✓</span><div><strong>Contents improved</strong><span>Abstract and appendices included.</span></div></div><div class="check"><span class="mark">✓</span><div><strong>Canonical URLs corrected</strong><span>Repository rename propagated into the publication.</span></div></div><div class="check"><span class="mark">✓</span><div><strong>Build pinned</strong><span>PDF generation uses a fixed ReportLab version for reproducibility.</span></div></div></div></div>`
  },
  {
    label:'VERIFICATION',
    html:`<div class="scene-inner"><p class="eyebrow">Principle XIX · Build for Inspection</p><h2>The corrected artifact was checked again.</h2><div class="metric-row"><div class="metric"><b>21</b><span>pages rendered</span></div><div class="metric"><b>0</b><span>known layout defects remaining</span></div><div class="metric"><b>1</b><span>verified publication artifact</span></div></div><p class="lead">The PDF was opened, rendered, and checked for clipping, overlap, malformed tables, broken glyphs, and bad page breaks.</p></div>`
  },
  {
    label:'THE RESULT',
    html:`<div class="scene-inner"><p class="eyebrow">What DPP changed</p><div class="big-verdict">LOOKS DONE<br><span>→ ACTUALLY DONE.</span></div><p class="lead">DPP did not make the first artifact magically correct. It prevented an unverified artifact from being misrepresented as finished, forced inspection, exposed a real defect, and required correction before acceptance.</p><a class="evidence-link" href="DPP-Whitepaper-v1.0.pdf">Open the verified whitepaper PDF →</a></div>`
  }
];
let index=0, playing=true, timer;
const scene=document.getElementById('scene'), label=document.getElementById('stepLabel'), bar=document.getElementById('progressBar'), play=document.getElementById('playBtn');
function render(){scene.innerHTML=scenes[index].html;label.textContent=`${String(index+1).padStart(2,'0')} / ${String(scenes.length).padStart(2,'0')} · ${scenes[index].label}`;bar.style.width=`${((index+1)/scenes.length)*100}%`;}
function schedule(){clearTimeout(timer);if(playing)timer=setTimeout(()=>{index=(index+1)%scenes.length;render();schedule();},5200)}
function setPlay(v){playing=v;play.textContent=v?'Pause':'Play';schedule()}
document.getElementById('nextBtn').onclick=()=>{index=(index+1)%scenes.length;render();schedule()};
document.getElementById('prevBtn').onclick=()=>{index=(index-1+scenes.length)%scenes.length;render();schedule()};
play.onclick=()=>setPlay(!playing);
document.addEventListener('keydown',e=>{if(e.key==='ArrowRight')document.getElementById('nextBtn').click();if(e.key==='ArrowLeft')document.getElementById('prevBtn').click();if(e.key===' ') {e.preventDefault();play.click();}});
render();schedule();