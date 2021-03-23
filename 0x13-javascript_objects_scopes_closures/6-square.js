#!/usr/bin/node
const SquareParent = require('./5-square.js');

module.exports = class Square extends SquareParent {
  constructor (size) {
    super(size, size);
  }

  charPrint (c) {
    c = c === undefined ? c = 'X' : c;
    for (let i = 0; i < this.height; i++) {
      let row = '';
      for (let j = 0; j < this.width; j++) {
        row += c;
      }
      console.log(row);
    }
  }
};
