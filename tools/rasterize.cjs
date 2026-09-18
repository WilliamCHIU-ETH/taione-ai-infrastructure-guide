// Usage: NODE_PATH=<directory containing sharp> node tools/rasterize.cjs
const fs=require('node:fs');
const path=require('node:path');
const sharp=require('sharp');
const dir=path.join(__dirname,'../assets/figures');
(async()=>{
  for(const name of fs.readdirSync(dir).filter(x=>x.endsWith('.svg'))){
    const input=path.join(dir,name),output=input.replace(/\.svg$/,'.png');
    await sharp(input,{density:144}).png().toFile(output);
    console.log(path.basename(output));
  }
})();
