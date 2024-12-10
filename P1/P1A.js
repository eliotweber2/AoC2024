const fs = require('fs');

const test = fs.readFileSync('./Input.txt',{ encoding: 'utf8', flag: 'r' });

function formatLsts(textLsts) {
    const lines = textLsts.split('\n');
    const lst1 = lines.map(line => line.slice(0,5) * 1);
    const lst2 = lines.map(line => line.slice(8) * 1);
    return [lst1,lst2];
}

const [lst1,lst2] = formatLsts(test);

lst1.sort();
lst2.sort();

const dsts = lst1.map((val,ind) => Math.abs(val-lst2[ind]));
console.log(dsts.reduce((a,b) => a+b));