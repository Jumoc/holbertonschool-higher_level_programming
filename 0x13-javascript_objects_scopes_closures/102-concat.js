#!/usr/bin/node
const fs = require('fs');

try {
  const file1 = fs.readFileSync(process.argv[2], 'utf8');
  const file2 = fs.readFileSync(process.argv[3], 'utf8');
  const data = file1 + '\n' + file2 + '\n';
  fs.writeFileSync(process.argv[4], data);
} catch (err) {
  console.error(err);
}
