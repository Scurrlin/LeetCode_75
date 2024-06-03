class Trie:

    def __init__(self):
        self.root={}
        
    def insert(self, word: str) -> None:

        curr=self.root

        for letter in word:
            if letter not in curr:
                curr[letter]={}
            curr=curr[letter]

        curr['*']=''

    def search(self, word: str) -> bool:

        curr=self.root
        for letter in word:
            if letter not in curr:
                return False
            curr=curr[letter]

        return '*' in curr
        
    def startsWith(self, prefix: str) -> bool:

        curr=self.root
        for letter in prefix:
            if letter not in curr:
                return False
            curr=curr[letter]

        return True