const fs = require('fs');

const example = '12345';
const example2 = '2333133121414131402'

str = fs.readFileSync('./Input9.txt','utf8');

function parse(str) {
  let id = 0;
  const lst = [];
  const gaps = [];
  const files = [];
  let isFile = true;
  for (let num of str) {
    if (!isFile && parseInt(num) != 0) {
      gaps.push([lst.length, lst.length+parseInt(num)]);
    } else if (isFile) {
      files.push([lst.length, lst.length+parseInt(num)]);
    }
    for (let i = 0; i < parseInt(num); i++) {
      if (isFile) {
        lst.push(id);
      } else {
        lst.push('.');
      }
    }
    if (isFile) {
        id++;
    }
    isFile = !isFile;
  }
  return [lst,gaps,files];
}

function fitFile(lst,gaps,file) {
  //console.log(file,lst[file[0]]);
  for (let gi = 0; gi < gaps.filter(gap => gap[0] < file[0]).length; gi++) {
    if (file[1] - file[0] <= gaps[gi][1] - gaps[gi][0]) {
      const fileId = lst[file[0]];
      //console.log(gaps[gi],file);
      for (let i = gaps[gi][0]; i < gaps[gi][0] + (file[1] - file[0]); i++) {
        lst.splice(i,1,fileId)
      }
      for (let i = file[0]; i < file[1]; i++) {
        lst.splice(i,1,'.');
      }
      
      return [lst,gi];
    }
  }
  return [lst,-1];
}

function compress(lst,gaps,files) {
  for (let file of files.toReversed()) {
    if (files.indexOf(file) % 100 == 0) {
      console.log(files.indexOf(file));
    }
    let gi;
    [lst,gi] = fitFile(lst,gaps,file);
    if (gi != -1) {
        const diff = (gaps[gi][1] - gaps[gi][0]) - (file[1] - file[0]);
        if (diff != 0) {
            gaps.splice(gi+1,0,[gaps[gi][1] - diff, gaps[gi][1]]);
        }
        gaps.splice(gi,1);
    }
    //console.log(lst);
  }
  return lst
}

function calc(lst) {
    return lst.map((x,ind) => x == '.'? 0 : x * ind).reduce((a,b) => a + b)
}

const [lst,gaps,files] = parse(str);
//console.log(gaps,files);
//console.log('hi');
const compressed = compress(lst,gaps,files);
//console.log('hi');
//console.log(compressed);
console.log(calc(compressed));


