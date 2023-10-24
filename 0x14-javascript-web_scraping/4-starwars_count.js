#!/usr/bin/node
const request = require('request');

// Check if the URL is provided as a command-line argument
if (process.argv.length !== 3) {
  console.error('Usage: ./3-starwars_count.js <URL>');
  process.exit(1);
}

const apiUrl = process.argv[2];

request(apiUrl, (error, response, body) => {
  if (error) {
    console.error(error);
  } else if (response.statusCode !== 200) {
    console.error(`Error: ${response.statusCode}`);
  } else {
    const filmData = JSON.parse(body);
    const wedgeAntillesFilms = filmData.results.reduce((count, film) => {
      const hasWedgeAntilles = film.characters.some((character) => character.endsWith('/18/'));
      return count + (hasWedgeAntilles ? 1 : 0);
    }, 0);
    console.log(wedgeAntillesFilms);
  }
});
