# Scripts to beat the New York Times Spelling Bee, Wordle, and LetterBoxed Puzzles
Ever had a boss, colleague, or friend challenge you to a New York Times puzzling marathon? If so, these little scripts are for you. Download these little scripts and run them on google.colab or your own machine with Python 3.9 and above. They are published in notebook format (ipynb) and packaged for the command line (py). Go keep pace with even the most experienced puzzlers...

## Dictionaries
You'll need to load a dictionary to power these scripts. The New York Times puzzles use the Oxford English Dictionary (~600,000 words) exclusively (but it costs money). If a word is not accepted by a NYT game, it's absence from the Oxford Dictionary or different spelling are usually the culprit. 
* Oxford Dictionary Personal Subscriptions are available here: https://www.oed.com/information/purchasing/individual-subscriptions/
* No, I do not believe they allow you to download the wordlist. 

Workarounds: The scripts below have free but incomplete dictionaries preloaded into them (~45K to ~145K wordlists). If you want more words, I suggest the RIDYHEW (ridiculously huge English word list with ~475,000 words) as another free alternative. RIDYHEW is a word list consisting of all words used in literature going back centuries. As such, many of the words in RIDYHEW are not up to the spelling standards of the Oxford English Dictionary. 
* You can find the RIDYHEW word list here: https://codehappy.net/wordlist.htm
* You are welcome to use any dictionary you see fit, you'll see that I've used multiple in these scripts and turn them on and off by commenting out the load scripts...

## LetterBoxed:
The objective of LetterBoxed is use of each of the given letters, in as few words as possible. The understated goal is to solve the puzzle with only two words. Words must be at least 3 letters long. Letters can be reused, but consecutive letters cannot be from the same side. This script benefits most from the larger RIDYHEW dictionary, and is often able to find a solution with the fewest number of words using all the letters. 
* Typically this script will find multiple solutions
* Remember: Not all RIDYHEW dictionary words are legal for this game, the free dictionaries are incomplete, and the Oxford Dictionary costs you money.

## Spelling Bee
Spelling Bee is a word game that puts your vocabulary skills to the test. The game presents a set of pre-selected letters, and your goal is to create as many words as possible using these letters. However, there's a twist: each word must include the center letter provided in the puzzle. For each daily puzzle, a list of words is carefully curated by the editors. Your task is to find as many words as you can with the given letters, making sure to include the center letter in each word. This game is perfect for word game enthusiasts and anyone looking to improve their vocabulary and word recognition skills.
* Typically this script will find the majority of the curated words with the Free Scrabble Dictionary (~145K words) despite being incomplete.
* Not all RIDYHEW dictionary words are legal for this game and the Oxford Dictionary costs you money.

## Wordle
Wordle is a daily word-guessing game where you try to find a new five-letter word within six attempts. With each guess, you gain a little more information, helping you narrow down your options and eventually discover the correct answer. Everybody playing on any given day is looking for the same word. Wordle can be played online through the official Wordle website or the New York Times' Crossword app, available for both iOS and Android devices. It's completely free to play. However, if you want to access the WordleBot helper tool, you'll need to pay a fee. This code saved more than a few people's win streaks.
* This script will narrow down your options with each bit of new data given
* You'll have to order the letters yourself...
* Repeat step 4 as many times as you need to (you only get 6 tries)...
* Remember: Not all RIDYHEW dictionary words are legal for this game, the free dictionaries are incomplete, and the Oxford Dictionary costs you money.

## Why Were These Written?
A python professor challenged me to use my time (in class) to prove that I understood the concepts he was teaching. He asked that I find and implement a real world scenario. At the same time (2021-2022) Wordle was released and many students were playing with their phones during same said class. Once the Wordle Solver was written, two ESL students asked if I could build the other two. The subsequent use case for these scripts is a fun way to increase English vocabulary. I share them here out of courtesy.
