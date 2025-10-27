# A trie (pronounced as "try") or prefix tree is a tree data structure used to
# efficiently store and retrieve keys in a dataset of strings. There are various
# applications of this data structure, such as autocomplete and spellchecker.

# Implement the Trie class:

# Trie() Initializes the trie object. void insert(String word) Inserts the
# string word into the trie. boolean search(String word) Returns true if the
# string word is in the trie (i.e., was inserted before), and false otherwise.
# boolean startsWith(String prefix) Returns true if there is a previously
# inserted string word that has the prefix prefix, and false otherwise.

class Trie:
    def __init__(self):
        self.root = {}
        
    def insert(self, word: str) -> None:
        curr = self.root
        for letter in word:
            if letter not in curr:
                curr[letter] = {}
            curr = curr[letter]
        curr['*'] = ''

    def search(self, word: str) -> bool:
        curr = self.root
        for letter in word:
            if letter not in curr:
                return False
            curr = curr[letter]
        return '*' in curr
        
    def startsWith(self, prefix: str) -> bool:
        curr = self.root
        for letter in prefix:
            if letter not in curr:
                return False
            curr = curr[letter]
        return True