import random
from words import wordlist

word = random.choice(wordlist).upper()
crtice = ("_" * (len(word)))

"""print(word)
print(crtice)"""

guess = input("Type your word or letter ").upper()

