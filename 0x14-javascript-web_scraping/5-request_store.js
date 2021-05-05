#!/usr/bin/node
const request = require('request');
const process = require('process');
const fs = require('fs');

const url = process.argv[2];
const filePath = process.argv[3];

request(url, (err, resp, body) => {
  if (err) console.error(err);
  // console.log(JSON.parse(body));
  fs.writeFile(filePath, body, 'utf-8', (err) => {
    if (err) {
      return console.error(err);
    }
  });
});
