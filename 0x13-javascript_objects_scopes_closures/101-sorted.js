#!/usr/bin/node
const dict = require('./101-data.js').dict;
const newDict = {};

for (const id in dict) {
  if (newDict[dict[id]] === undefined) {
    newDict[dict[id]] = [id];
  } else {
    newDict[dict[id]].push(id);
  }
}
console.log(newDict);
