"""Write a Python program that reads a text input from the user and counts the frequency of each word in the text.

The program should ignore case, punctuation, and count words accurately. 
The output should be a list of words sorted by frequency, with the most frequent words appearing first.

"""

wordcount = {}


def count(sentence):
    for word in sentence.split():
        word = word.lower()
        if word in wordcount:
            wordcount[word] += 1
        else:
            wordcount[word] = 1
    return wordcount


sentence = input("Enter a sentence: ")
wordcount = count(sentence)
print(f"List of words: {wordcount}")
