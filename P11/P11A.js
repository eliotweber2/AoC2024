const example = [125,17];

const memo = {};

let stoneCt = 0;
let cacheHits = 0;

function getNext(stone) {
  if (stone == 0) {
    return [1];
  }
  if ((stone + '').length % 2 == 0) {
    return split(stone);
  }
  return [stone * 2024];
}

function split(stone) {
  const str = stone + '';
  return [parseInt(str.slice(0,str.length/2)), parseInt(str.slice(str.length/2,str.length))];
}

function resolve(stone,ct,end) {
  const cacheCheck = stone + ' ' + ct;
  if (cacheCheck in memo) {
    cacheHits++;
    return memo[cacheCheck];
  }
  
  if (ct == end) {
    stoneCt++;
    return 1
  }
  
  const next = getNext(stone);
  //console.log(next,ct);
  let finishCt = 0;
  for (let nextStone of next) {
    finishCt += resolve(nextStone,ct+1,end);
  }
  memo[stone + ' ' + ct] = finishCt;
  return finishCt;
}

let tot = 0;
const example2 = ['3028','78','973951','5146801','5','0','23533','857'];
for (let stone of example2) {
  const out = resolve(stone,0,25);
  //console.log(out);
  tot += out;
}

console.log(tot);
//console.log(cacheHits);
//console.log(memo);


