// GetRandom Words from API and push to Array
async function getRandomWord() {

  const res = await fetch('https://random-words-api.vercel.app/word');

  const data = await res.json();
  return data[Object.keys(data)[0]].word.toLowerCase();

}

getRandomWord();

// Add Word to DOM
async function addWordToDOM() {
  randomWord = await getRandomWord();
  word.innerHTML = randomWord;
}