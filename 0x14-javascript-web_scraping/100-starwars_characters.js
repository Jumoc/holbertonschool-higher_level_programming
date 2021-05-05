#!/usr/bin/node
const request = require('request');
const process = require('process');

const id = process.argv[2];
const url = `https://swapi-api.hbtn.io/api/films/${id}/`;

request(url, (err, resp, body) => {
  if (err) console.error(err);
  // console.log(JSON.parse(body));
  for (const element of JSON.parse(body).characters) {
    request(element, (err, resp, body) => {
      if (err) console.error(err);
      console.log(JSON.parse(body).name);
    });
  }
});
