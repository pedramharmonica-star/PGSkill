const {chromium}=require('playwright');
(async()=>{const b=await chromium.launch();const p=await b.newPage({viewport:{width:1920,height:1080}});
await p.goto('file://'+process.cwd()+'/'+(process.argv[2]||'proposal.html'));await p.evaluate(()=>document.fonts.ready);await p.waitForTimeout(800);
const n=await p.evaluate(()=>document.querySelectorAll('.page').length);
const fs=require('fs'); fs.mkdirSync('png',{recursive:true});
for(let i=0;i<n;i++){const el=(await p.$$('.page'))[i]; await el.screenshot({path:`png/p${String(i+1).padStart(2,'0')}.png`});}
await p.pdf({path:(process.argv[3]||'PayamGostar-Proposal-Sarzamin.pdf')+'',width:'1920px',height:'1080px',printBackground:true,preferCSSPageSize:true});
await b.close(); console.log(n);})();
