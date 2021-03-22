#!/usr/bin/node
const n1 = parseInt(process.argv[2]);
const n2 = parseInt(process.argv[3]);

if (isNaN(n1) || isNaN(n2)) {
  console.log('NaN');
} else {
  console.log(n1 + n2);
}
