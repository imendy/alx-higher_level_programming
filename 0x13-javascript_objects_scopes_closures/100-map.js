#!/usr/bin/node
let list = require('./100-data').list;
let newList = list.map((current, index) => {
  return (current * index);
});
console.log(list);
console.log(newList);
