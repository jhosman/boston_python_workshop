import re
import scrabble

# unma
pattern = re.compile("unmois")
for word in scrabble.wordlist:
    if pattern.search(word):
        print word
