#!/usr/bin/node
exports.nbOccurences = function (list, searchElement) {
  let counter = 0;
  for (const number of list) {
    if (number === searchElement) { counter++; }
  }
  return counter;
};
