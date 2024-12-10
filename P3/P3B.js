const fs = require('fs');

const str = fs.readFileSync('./Input3.txt', 'utf8');

function reSplit(str) {
  return str.split('\n').join('');
}

function processMatch(mul) {
  const numRegex = /\d+,\d+/;
  const nums = Array.from(mul.match(numRegex)).map(match => match.split(',').map(x => x*1).reduce((a,b) => a*b));
  return nums;
}

function sliceString(str) {
  const doRegex = /(?:do\(\)|don't\(\))/g;
  let state = 1;
  let lastInd = 0;
  let ct = 0
  while ((nextStatement = doRegex.exec(str)) != null) {
    if (nextStatement[0] == 'don\'t()') {
      ct++;
      if (state == 1) {
        lastInd = nextStatement.index;
      }
      state = 0;
    } else {
      if (state == 0) {
        str = str.slice(0,lastInd) + str.slice(doRegex.lastIndex);
        doRegex.lastIndex -= (doRegex.lastIndex - lastInd);
      }
      state = 1;
    }
  }
  return str;
}

const regex = /mul\(\d+,\d+\)/g;

let newStr = reSplit(str);

newStr = sliceString(newStr);

const muls = newStr.match(regex);

const sum = muls.map(x => processMatch(x)).flat().reduce((a,b) => a+b);

console.log(sum);