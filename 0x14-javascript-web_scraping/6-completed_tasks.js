#!/usr/bin/node
const request = require('request');
const process = require('process');

const url = process.argv[2];

request(url, (err, resp, body) => {
  if (err) console.error(err);
  // console.log(JSON.parse(body));
  const tasksId = {};
  for (const element of JSON.parse(body)) {
    if (element.completed) {
      if (tasksId[`${element.userId}`] === undefined) { tasksId[`${element.userId}`] = 1; } else { tasksId[`${element.userId}`] = tasksId[`${element.userId}`] + 1; }
    }
  }
  console.log(tasksId);
});
