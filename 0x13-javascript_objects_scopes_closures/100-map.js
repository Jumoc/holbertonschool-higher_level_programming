#!/usr/bin/node
const list = require('./100-data.js').list;
let idx = 0;
const arr = list.map(x => x * idx++);
console.log(list);
console.log(arr);
