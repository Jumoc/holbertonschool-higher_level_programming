#!/usr/bin/node
const number = parseInt(process.argv[2]);
let row = '';

if (isNaN(number)) {
  console.log('Missing size');
} else {
  for (let i = 0; i < number; i++) {
      row = '';
    for (let j = 0; j < number; j++) {
        row += '#'
    }
    console.log(row);
  }
}
