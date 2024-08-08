#!/usr/bin/node

const util = require('util');
const request = util.promisify(require('request'));

const filmID = process.argv[2];

if (!filmID) {
  console.error('Error: Please provide a valid Star Wars movie ID.');
  process.exit(1);
}

async function fetchJSON(url) {
  try {
    const response = await request(url);
    return JSON.parse(response.body);
  } catch (error) {
    console.error(`Error fetching data from ${url}:`, error.message);
    process.exit(1);
  }
}

async function fetchCharacters(characterUrls) {
  const characterPromises = characterUrls.map(url => fetchJSON(url));
  return await Promise.all(characterPromises);
}

async function printCharacters(filmId) {
  const filmUrl = `https://swapi-api.hbtn.io/api/films/${filmId}/`;
  const filmData = await fetchJSON(filmUrl);
  const characters = await fetchCharacters(filmData.characters);

  characters.forEach(character => {
    console.log(character.name);
  });
}

printCharacters(filmID);
