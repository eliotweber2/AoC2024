const fs = require('fs');

const example = '12345';
const example2 = '2333133121414131402'

str = fs.readFileSync('./Input9.txt','utf8');

function parse(str) {
  let id = 0;
  const lst = [];
  const gaps = [];
  let isFile = true;
  for (let num of str) {
    if (!isFile && parseInt(num) != 0) {
      gaps.push([lst.length, lst.length+parseInt(num)]);
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
  return [lst,gaps];
}

function compress(lst,gaps) {
  for (let gap of gaps) {
    const paste = [];
    for (let i = 0; i < gap[1] - gap[0]; i++) {
      let test = lst.pop();
      //console.log(i,lst);
      if (test ==  '.') {
        i--;
        if (gap == gaps[gaps.length-1]) {
            return lst;
        }
        gaps.pop();
        lst = removeLast(lst);
        //console.log('hi',lst)
      } else {
        lst[gap[0] + i] = test;
      }
    }
  }
  return lst;
}

function calc(lst) {
    return lst.map((x,ind) => x == '.'? 0 : x * ind).reduce((a,b) => a + b)
}

function removeLast(lst) {
    let i = lst.length-1;
    while (true) {
        if (lst[i] == '.') {
            lst.pop();
        } else {
            return lst;
        }
        i--
    }
}

const [lst,gaps] = parse(str);
//console.log(lst,gaps);
const compressed = compress(lst,gaps)
//console.log(compressed);
console.log(calc(compressed));


