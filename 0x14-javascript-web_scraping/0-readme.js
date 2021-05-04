#!/usr/bin/node
const fs = require('fs');
const process = require('process');

const filePath = process.argv[2];

fs.readFile(filePath, 'utf-8', (err, data) => {
  if (err) {
    return console.error(err);
  }
  console.log(data);
});
