#!/usr/bin/node
const fs = require('fs');

// Check if the file path is provided as a command-line argument
if (process.argv.length !== 4) {
  console.error('Usage: node 1-writeme.js <file-path> "content"');
  process.exit(1);
}

const filePath = process.argv[2];
const contentToWrite = process.argv[3];

fs.writeFile(filePath, contentToWrite, 'utf-8', err => {
  if (err) {
    console.error(err);
  }
});
