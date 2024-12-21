const fs = require('fs');

const input = fs.readFileSync('Input19.txt').toString();

const example_input = `r, wr, b, g, bwu, rb, gb, br

brwrr
bggr
gbbr
rrbgbr
ubwu
bwurrg
brgr
bbrgwb`

function parse(input) {
  const patterns = input.split('\n\n')[0].split(', ');
  const towels = input.split('\n\n')[1].split('\n');
  return [patterns,towels];
}

function match(inputLst,towel) {
  //console.log(towel);
  if (towel.length == 0) {
    return true;
  }
  for (let poss of inputLst) {
    //console.log(poss);
    if (poss.length > towel.length) {
      continue;
    }
    let failed = false;
    for (let i = 0; i < poss.length; i++) {
      if (towel[i] != poss[i]) {
        failed = true;
        break;
      }
    }
    if (!failed) {
      if (match(inputLst,towel.slice(poss.length,towel.length))) {
        return true;
      }
    }
  }
  return false;
}

function minimizeInput(patterns) {
  patterns.sort((a,b) => b.length - a.length);
  for (let i = 0; i < patterns.length; i++) {
    pattern = patterns[i];
    patterns.splice(i,1);
    //console.log(pattern,patterns)
    if (!match(patterns,pattern)) {
      patterns.splice(i,0,pattern);
    } else {
      i--;
    }
  }
  return patterns;
}

let [patterns,towels] = parse(input);

let ct = 0;
patterns = minimizeInput(patterns);
for (let towel of towels) {
  if (match(patterns,towel)) {
    ct++;
  } else {
    console.log(towel);
  }
}

console.log('hi',patterns);
console.log(ct);


