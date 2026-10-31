const {chromium}=require('playwright');
(async()=>{const b=await chromium.launch();const p=await b.newPage({viewport:{width:1920,height:1080}});
await p.goto('file://'+process.cwd()+'/slide.html');await p.evaluate(()=>document.fonts.ready);await p.waitForTimeout(400);
await p.screenshot({path:'slide-test.png'});await b.close();})();
