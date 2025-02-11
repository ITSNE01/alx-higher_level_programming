#!/usr/bin/node

const request = require('request');

const apiUrl = process.argv[2];

if (!apiUrl) {
  console.error('Usage: node 4-starwars_count.js <API_URL>');
  process.exit(1);
}

request(apiUrl, (error, response, body) => {
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
    const films = data.results;
    const wedgeId = '18';
    
    const count = films.filter(film => 
      film.characters.some(character => character.includes(`/people/${wedgeId}/`))
    ).length;

    console.log(count);
  } catch (parseError) {
    console.error('Error parsing JSON:', parseError);
  }
});
