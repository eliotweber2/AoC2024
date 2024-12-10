const fs = require('fs');

const test = fs.readFileSync('./Input.txt',{ encoding: 'utf8', flag: 'r' });

function formatLsts(textLsts) {
    const lines = textLsts.split('\n');
    const lst1 = lines.map(line => line.slice(0,5) * 1);
    const lst2 = lines.map(line => line.slice(8) * 1);
    return [lst1,lst2];
}

const [lst1,lst2] = formatLsts(test);


let count = 0;

lst1.forEach(ele => count += lst2.filter(x => x == ele).length * ele);

console.log(count);