#!/usr/bin/env node

const util = require('util');
const request = util.promisify(require('request'));

const filmID = process.argv[2];

async function fetchCharacter(url) {
  try {
    let character = await (await request(url)).body;
    return JSON.parse(character).name;
  } catch (error) {
    console.error(`Failed to fetch character at ${url}:`, error);
    return null;
  }
}

async function fetchFilmDetails(filmId) {
  const endpoint = `https://swapi-api.hbtn.io/api/films/${filmId}`;
  try {
    let response = await (await request(endpoint)).body;
    return JSON.parse(response);
  } catch (error) {
    console.error(`Failed to fetch film details for film ID ${filmId}:`, error);
    process.exit(1);
  }
}

async function displayCharacters(characterUrls) {
  console.log('Fetching character names, please wait...\n');
  const promises = characterUrls.map(fetchCharacter);
  const characterNames = await Promise.all(promises);

  characterNames.forEach((name, index) => {
    if (name) {
      console.log(`${index + 1}. ${name}`);
    }
  });
}

async function starwarsCharacters(filmId) {
  const filmDetails = await fetchFilmDetails(filmId);
  const characterUrls = filmDetails.characters;
  await displayCharacters(characterUrls);
}

if (!filmID) {
  console.error('Please provide a valid Star Wars movie ID.');
  process.exit(1);
}

starwarsCharacters(filmID);
