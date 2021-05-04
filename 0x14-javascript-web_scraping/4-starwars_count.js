#!/usr/bin/node
const request = require('request');
const process = require('process');

const url = process.argv[2];

request(url, (err, resp, body) => {
  if (err) console.error(err);
  // console.log(JSON.parse(body));
  let counter = 0;
  for (const result of JSON.parse(body).results) {
      result.characters.forEach(element => {
          if (element.includes('18')) {
              counter++;
          }
      });
  }
  console.log(counter);
});
