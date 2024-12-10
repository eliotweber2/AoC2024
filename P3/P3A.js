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

const regex = /mul\(\d+,\d+\)/g;

const newStr = reSplit(str);

const muls = newStr.match(regex);

const sum = muls.map(x => processMatch(x)).flat().reduce((a,b) => a+b);

console.log(sum);

