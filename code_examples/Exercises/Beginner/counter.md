# Exercise Statement: Word Frequency Counter

**Objective:** Write a Python program that reads a text input from the user and counts the frequency of each word in the text.

## Requirements:
1. The program should ignore case sensitivity, meaning "Word" and "word" should be treated as the same word.
2. Punctuation should be ignored, so words like "hello," and "hello" should be considered identical.
3. The output should be a list of words sorted by their frequency, with the most frequent words appearing first.

## Instructions:
- Create a function named `count(sentence)` that takes a string input (the sentence) and returns a dictionary containing each unique word as the key and its corresponding frequency as the value.
- After obtaining the input from the user, call the `count` function to compute the frequencies.
- Finally, print the word frequency dictionary and the list of words sorted by their frequency in descending order.
