const fs = require('fs');

const real = fs.readFileSync('./Input13.txt','utf8');

const strExample = `Button A: X+94, Y+34
Button B: X+22, Y+67
Prize: X=8400, Y=5400

Button A: X+26, Y+66
Button B: X+67, Y+21
Prize: X=12748, Y=12176

Button A: X+17, Y+86
Button B: X+84, Y+37
Prize: X=7870, Y=6450

Button A: X+69, Y+23
Button B: X+27, Y+71
Prize: X=18641, Y=10279`

function parse(str) {
  const examples = str.split('\n\n');
  const lst = [];
  for (let example of examples) {
    const pairs = example.split('\n').map(line => line.match(/\d+/g));
    const buttonA = pairs[0].map(n => parseInt(n));
    const buttonB = pairs[1].map(n => parseInt(n));
    const prize = pairs[2].map(n => parseInt(n));
    lst.push({buttonA: buttonA, buttonB: buttonB, prize: prize});
  }
  return lst;
}

function findValidMult(check) {
  const valid = [];
  //const startButton = check.buttonA[0] > check.buttonB[0]? check.buttonA : check.buttonB;
  //const second = check.buttonA[0] < check.buttonB[0]? check.buttonA : check.buttonB;
  startButton = check.buttonA;
  second = check.buttonB;
  let mult = Math.floor(check.prize[0] / startButton[0]) > 100? 100 : Math.floor(check.prize[0] / startButton[0])
  while (mult >= 0) {
    if (Number.isInteger((check.prize[0] - startButton[0] * mult)  / second[0])) {
      if ((check.prize[0] - startButton[0] * mult)  / second[0] <= 100)
      valid.push([mult,(check.prize[0] - startButton[0] * mult)  / second[0]]);
    }
    mult--;
  }
  const yvalid = [];
  for (let poss of valid) {
    if (startButton[1] * poss[0] + second[1] * poss[1] == check.prize[1]) {
      if (startButton == check.buttonA) {
        yvalid.push(poss);
      } else {
        yvalid.push(poss.toReversed());
      }
    }
  }
  return yvalid;
}

function isInt(i) {
  return i % 1 == i;
}

const example = parse(real);
tot = 0;
for (let check of example) {
  const results = findValidMult(check);
  if (results.length == 0) {
    continue;
  }
  //console.log(results);
  tot += results[0][0] * 3 + results[0][1] * 1;
}

console.log(tot);


