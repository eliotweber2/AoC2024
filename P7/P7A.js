const fs = require('fs');

const input = fs.readFileSync('./input7.txt', 'utf8');

const example = `190: 10 19
3267: 81 40 27
83: 17 5
156: 15 6
7290: 6 8 6 15
161011: 16 10 13
192: 17 8 14
21037: 9 7 18 13
292: 11 6 16 20`

function eval(nums,ops) {
    let curr = 0;
    for (let i = 0; i < nums.length; i++) {
        if (curr == 0) {
            curr = nums[i];
        } else if (ops[i-1] == '+') {
            curr += nums[i];
        } else {
            curr *= nums[i];
        }
        if (i > ops.length-1) {
            return curr;
        }
    }
    return curr;
}

function parse(str) {
    const lines = str.split('\n');
    const lineLst = [];
    for (let line of lines) {
        let tgt = parseInt(line.split(':')[0]);
        let nums = line.split(': ')[1].split(' ').map(x => parseInt(x));
        lineLst.push({tgt:tgt,nums:nums});
    }
    return lineLst;
}

function findOps(nums,ops,tgt) {
    const orig = ops.length;
    if (eval(nums,ops) > tgt) {
        return false;
    }
    if (ops.length == nums.length-1) {
        return eval(nums,ops) == tgt;
    }
    ops.push('*');
    if (findOps(nums,ops,tgt)) {
        return true;
    }
    ops = ops.slice(0,orig);
    ops.push('+');
    if (findOps(nums,ops,tgt)) {
        return true;
    }
    return false;
}

function run(lines) {
    let tot = 0;
    for (let line of lines) {
        if (findOps(line.nums, [], line.tgt)) {
            tot += line.tgt;
        }
    }
    return tot;
}

const exampleLines = parse(input);
console.log(run(exampleLines));
