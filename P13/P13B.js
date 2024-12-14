const fs = require('fs');
const Fraction = require('fraction.js');
const { default: test } = require('node:test');

const buttonA = [63,26];
const buttonB = [41,75];
const tgt = [3388,3431];

const real = fs.readFileSync('./Input13.txt','utf8');

const testStr = `Button A: X+94, Y+34
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

function solve(buttonA, buttonB, tgt) {
    const eqA = [buttonA[0], buttonB[0], tgt[0]];
    const eqB = [buttonA[1], buttonB[1], tgt[1]];
    const mA = new Fraction(eqA[0],eqB[0]);
    const mB = new Fraction(eqA[1],eqB[1]);
    return [solveEq(eqA,eqB,mB),solveEq(eqA,eqB,mA)];
}

function solveEq(eqA,eqB,m) {
    const result = eqA.map((x,i) => x - m.mul(eqB[i])).filter(x =>  x != 0);
    return result[1]/result[0]
}

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

const machines = parse(real);
let tot = 0;
const tol = 0.0001;
//console.log(solve(buttonA,buttonB,tgt));

for (let machine of machines) {
    machine.prize[0] += 10000000000000;
    machine.prize[1] += 10000000000000;
    let [a,b] = solve(machine.buttonA, machine.buttonB, machine.prize);
    if (Math.abs(a - Math.round(a)) < tol && Math.abs(b - Math.round(b)) < tol) {
        a = Math.round(a);
        b = Math.round(b);
        //console.log(machine.buttonA,machine.buttonB,machine.prize);
        console.log(a,b,3*a + b);
        tot += 3*a + b;
    }
}
console.log(tot);
