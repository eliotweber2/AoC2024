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

function makeGraph(patterns,towel) {
    const graph = {};
    const edgeLst = []; 
    const currLengths = [0];
    while (currLengths.length > 0) {
        const currLength = currLengths.pop();
        for (let i = 0; i < patterns.length; i++) {
            if (towel.length >= currLength + patterns[i].length && towel.slice(currLength,currLength+patterns[i].length) == patterns[i]) {
                if (!Object.keys(graph).includes(currLength.toString())) {
                    graph[currLength] = [currLength+patterns[i].length];
                    currLengths.unshift(currLength+patterns[i].length);
                    currLengths.unshift(currLength);
                } else {
                    const edges = edgeLst.filter((edge) => edge[0] == currLength && edge[1] == currLength+patterns[i].length);
                    if (edges.length == 0) {
                        if (!graph[currLength].includes(currLength+patterns[i].length)) {
                            graph[currLength].push(currLength+patterns[i].length);
                        }
                        edgeLst.push([currLength,currLength+patterns[i].length]);
                        currLengths.unshift(currLength+patterns[i].length);
                        currLengths.unshift(currLength);
                    }
                }
            }
        }
    }
    return graph;
}

function findNumPathsv2(graph, startNode, endIndex) {
    const memo = {};
    function dfs(node) {
        if (node == endIndex) {
            return 1;
        }
        if (node in memo) {
            return memo[node];
        }
        if (!(node in graph)) {
            return 0;
        }
        let numPaths = 0;
        for (let neighbor of graph[node]) {
            numPaths += dfs(neighbor);
        }
        memo[node] = numPaths;
        return numPaths;
    }
    return dfs(startNode);
}

const [patterns,towels] = parse(input);

/*
brwrr can be made in two different ways: b, r, wr, r or br, wr, r.
*/

ct = 0;
for (let towel of towels) {
    console.log(towel);
    const graph = makeGraph(patterns,towel);
    ct += findNumPathsv2(graph,0,towel.length);
}

console.log(ct);

/*
const towel = 'wburgwggguruuwbwwgbbrurbrrrgurugrrwwrwwgggbbbbrwwgug';
console.log(towel.length);
sortedPatterns = patterns.toSorted((a,b) => b.length - a.length);
const graph = makeGraph(patterns,towel);
console.log(graph);
console.log(findNumPathsv2(graph,0,towel.length));
*/