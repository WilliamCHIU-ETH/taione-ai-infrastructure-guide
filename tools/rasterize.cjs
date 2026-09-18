// Usage: NODE_PATH=<directory containing sharp> node tools/rasterize.cjs [figure-id ...]
// Without ids every SVG is rasterized; with ids (e.g. 06-a 06-b) only those are.
const fs=require('node:fs');
const path=require('node:path');
const sharp=require('sharp');
const dir=path.join(__dirname,'../assets/figures');
const only=process.argv.slice(2);
(async()=>{
  for(const name of fs.readdirSync(dir).filter(x=>x.endsWith('.svg')&&(!only.length||only.includes(x.replace(/\.svg$/,''))))){
    const input=path.join(dir,name),output=input.replace(/\.svg$/,'.png');
    await sharp(input,{density:144}).png().toFile(output);
    console.log(path.basename(output));
  }
})();
