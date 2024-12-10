const fs = require('fs');

const str = fs.readFileSync('./Input2.txt', 'utf8');

function getLines(str) {
  const lines = str.split('\n');
  const arrs = lines.map(line => line.split(' '));
  return arrs.map(arr => arr.map(i => i * 1))
}

function checkLine(line) {
  const ascending = arrsEqual(line.toSorted((a,b) => a - b), line);
  const descending = arrsEqual(line.toSorted((a,b) => b - a), line);
  if (!(ascending || descending)) {
    return false;
  }
  if (!checkPairs(line)) {
    return false;
  }
  return true;
}

function arrsEqual(arr1,arr2) {
  if (arr1.length == arr2.length && arr1.every((val,ind) => val == arr2[ind])) {
    return true;
  }
  return false;
}

function checkPairs(line) {
  for (let i = 0; i < line.length-1; i++) {
    if (Math.abs(line[i] - line[i+1]) > 3 || Math.abs(line[i] - line[i+1]) < 1) {
      return false;
    }
  }
  return true;
}

let correct = 0;
const lines = getLines(str);
for (let line of lines) {
  if (checkLine(line)) {
    correct++;
  }
}

console.log(correct);


