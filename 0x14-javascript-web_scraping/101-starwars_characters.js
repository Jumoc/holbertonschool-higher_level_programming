#!/usr/bin/node
const request = require('request');
const process = require('process');

const id = process.argv[2];
const link = `https://swapi-api.hbtn.io/api/films/${id}/`;

// Create a promise so we can do await on it
const doRequest = (url) => {
  return new Promise(function (resolve, reject) {
    request(url, (err, resp, body) => {
      if (err) reject(err);
      resolve(body);
    });
  });
};

async function main () {
  const res = await doRequest(link);
  for (const char of JSON.parse(res).characters) {
    const character = await doRequest(char);
    console.log(JSON.parse(character).name);
  }
}

main();
