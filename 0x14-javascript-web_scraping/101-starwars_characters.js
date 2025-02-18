#!/usr/bin/node

const request = require('request');

const url = 'https://swapi-api.hbtn.io/api/films/' + process.argv[2];

request(url, function (error, response, body) {
  if (!error) {
    const characters = JSON.parse(body).characters;
    printCharactersNames(characters, 0);
  }
});

function printCharactersNames (characters, index) {
  request(characters[index], function (error, response, body) {
    if (!error) {
      console.log(JSON.parse(body).name);
      if (index + 1 < characters.length) {
        printCharactersNames(characters, index + 1);
      }
    }
  });
}
