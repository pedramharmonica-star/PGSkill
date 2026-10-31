const {chromium}=require('playwright');
(async()=>{const b=await chromium.launch();const p=await b.newPage({viewport:{width:794,height:1123}});
await p.goto('file://'+process.cwd()+'/'+process.argv[2]);await p.evaluate(()=>document.fonts.ready);await p.waitForTimeout(600);
const n=await p.evaluate(()=>document.querySelectorAll('.a4').length);
for(let i=0;i<n;i++){const el=(await p.$$('.a4'))[i]; await el.screenshot({path:`pi${i+1}.png`});}
await p.pdf({path:process.argv[3],format:'A4',printBackground:true,preferCSSPageSize:true});
await b.close(); console.log(n);})();
