#!/usr/bin/node
const request = require('request');
const process = require('process');

const url = `https://swapi-api.hbtn.io/api/films/${process.argv[2]}`;

request(url, (err, resp, body) => {
  if (err) console.error(err);
  console.log(JSON.parse(body).title);
});
