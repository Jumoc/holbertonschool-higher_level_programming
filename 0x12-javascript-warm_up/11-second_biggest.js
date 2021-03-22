#!/usr/bin/node
if (process.argv.length <= 3) {
  console.log('0');
} else {
  process.argv.splice(0, 2);
  process.argv.sort(function (a, b) { return a - b; });
  console.log(process.argv[process.argv.length - 2]);
}
