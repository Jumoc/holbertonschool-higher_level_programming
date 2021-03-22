#!/usr/bin/node
const fact = function (num) {
  if (num === 1 || isNaN(num)) { return (1); }
  return (num * fact(num - 1));
};

console.log(fact(parseInt(process.argv[2])));
