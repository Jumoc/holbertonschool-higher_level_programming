#!/usr/bin/node
const fs = require('fs');
const process = require('process');

const filePath = process.argv[2];
const text = process.argv[3] + '\n';

fs.writeFile(filePath, text, (err) => {
  if (err) {
    return console.error(err);
  }
});
