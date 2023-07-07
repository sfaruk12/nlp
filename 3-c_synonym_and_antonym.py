#Write a program using python to find synonym and antonym of word "active" using Wordnet.

from nltk.corpus import wordnet
print( wordnet.synsets("active"))

print(wordnet.lemma('active.a.01.active').antonyms())