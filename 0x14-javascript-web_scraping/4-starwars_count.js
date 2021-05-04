#!/usr/bin/node
const request = require('request');
const process = require('process');

request('https://swapi-api.hbtn.io/api/people/18/', (err, resp, body) => {
  if (err) console.error(err);
  console.log(JSON.parse(body).films.length);
});
