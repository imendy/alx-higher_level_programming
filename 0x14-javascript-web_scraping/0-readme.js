#!/usr/bin/node
const fs = require('fs');

// Check if the file path is provided as a command-line argument
if (process.argv.length !== 3) {
  console.error('Usage: node 0-readme.js <file-path>');
  process.exit(1);
}

const filePath = process.argv[2];

fs.readFile(filePath, 'utf-8', (err, content) => {
  console.log(err || content);
});
