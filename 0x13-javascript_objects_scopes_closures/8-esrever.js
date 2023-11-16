#!/usr/bin/node
exports.esrever = function (list) {
  const rever = [];
  for (let i = 0; i < list.length; i++) {
    rever.unshift(list[i]);
  }
  return rever;
};
