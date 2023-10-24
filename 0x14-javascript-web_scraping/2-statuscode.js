#!/usr/bin/node
const request = require('request');

// Check if the url is provided as a command-line argument
if (process.argv.length !== 3) {
  console.error('Usage: ./2-statuscode.js url');
  process.exit(1);
}

const url = process.argv[2];

request(url, (err, response) => {
  if (err) {
    console.log(err);
  } else {
    console.log(`code: ${response.statusCode}`);
  }
});
