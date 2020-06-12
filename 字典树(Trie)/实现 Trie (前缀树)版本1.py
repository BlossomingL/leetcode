class Trie:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = {}
        self.end = '#'

    def insert(self, word):
        """
        Inserts a word into the trie.
        """
        node = self.root
        for c in word:
            if c not in node:
                node[c] = {}
            node = node[c]
        node[self.end] = True

    def search(self, word):
        """
        Returns if the word is in the trie.
        """
        node = self.root
        for c in word:
            if c not in node:
                return False
            node = node[c]
        return True if self.end in node else False

    def startsWith(self, prefix):
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        node = self.root
        for c in prefix:
            if c not in node:
                return False
            node = node[c]
        return True

# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)