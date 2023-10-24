#!/usr/bin/node
const request = require('request');

const movieId = process.argv[2];
const filmUrl = `https://swapi-api.hbtn.io/api/films/${movieId}`;

// Make a request to get film data
request(filmUrl, (error, response, filmBody) => {
  if (!error && response.statusCode === 200) {
    const characters = JSON.parse(filmBody).characters;
    // Start printing characters one by one
    printCharacters(characters, 0);
  }
});

// Function to print characters from the characters array
function printCharacters (characters, index) {
  if (index < characters.length) {
    const characterUrl = characters[index];
    // Make a request to get character data
    request(characterUrl, (error, response, characterBody) => {
      if (!error && response.statusCode === 200) {
        const characterData = JSON.parse(characterBody);
        console.log(characterData.name);
        // Move on to the next character
        printCharacters(characters, index + 1);
      }
    });
  }
};
