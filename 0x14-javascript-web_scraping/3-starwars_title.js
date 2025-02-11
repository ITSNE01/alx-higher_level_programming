#!/usr/bin/node

const request = require('request');

const movieId = process.argv[2];

if (!movieId) {
  console.error('Usage: node 3-starwars_title.js <movie_ID>');
  process.exit(1);
}

const url = `https://swapi-api.alx-tools.com/api/films/${movieId}`;

request(url, (error, response, body) => {
  if (error) {
    console.error(error);
    return;
  }

  if (response.statusCode !== 200) {
    console.error(`Error: Unable to fetch data (Status Code: ${response.statusCode})`);
    return;
  }

  try {
    const data = JSON.parse(body);
    console.log(data.title);
  } catch (parseError) {
    console.error('Error parsing JSON:', parseError);
  }
});
