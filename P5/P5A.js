const fs = require('fs');

const real = fs.readFileSync('./Input5.txt', 'utf8');


const example = `47|53
97|13
97|61
97|47
75|29
61|13
75|53
29|13
97|29
53|29
61|53
97|53
61|29
47|13
75|47
97|75
47|61
75|61
47|29
75|13
53|13

75,47,61,53,29
97,61,53,29,13
75,29,13
75,97,47,61,53
61,13,29
97,13,75,29,47`

function parse(str) {
  const [rules,seqs] = str.split('\n\n');
  const rulesLst = [];
  rules.split('\n').forEach(rule => rulesLst.push(rule.split('|').map(i => i * 1)));
  const seqLst = [];
  seqs.split('\n').forEach(seq => seqLst.push(seq.split(',').map(i => i * 1)));
  return [seqLst,rulesLst];
}

function checkInd(seq,i,rules) {
  const before = seq.slice(0,i);
  const after = seq.slice(i+1,seq.length);
  //console.log(seq,i,before,after);
  const newRules = rules.filter(rule => rule.includes(seq[i]));
  for (let rule of newRules) {
    if (rule[0] == seq[i]) {
      if (!after.includes(rule[1]) && seq.includes(rule[1])) {
        return false;
      }
    }
    else if (!before.includes(rule[0]) && seq.includes(rule[0])) {
      return false;
    }
  }
  return true;
}

function checkSeq(seq) {
  for (let i = 0; i < seq.length; i++) {
    if (!checkInd(seq,i,rulesLst)) {
      return 0;
    }
  }
  return seq[Math.floor(seq.length/2)];
}

const [seqLst,rulesLst] = parse(real);
let tot = 0;
seqLst.forEach(seq => tot += checkSeq(seq));
console.log(tot);

