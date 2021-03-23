#!/usr/bin/node
exports.callMeMoby = function (x, theFunction) {
  for (let i; i < x; i++) {
    theFunction();
  }
};
