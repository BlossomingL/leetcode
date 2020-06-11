class Node:
    def __init__(self):
        self.child = {}
        self.end = False


class WordDictionary:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = Node()

    def addWord(self, word):
        """
        Adds a word into the data structure.
        """
        node = self.root
        for c in word:
            if c not in node.child:
                node.child[c] = Node()
            node = node.child[c]
        node.end = True

    def search(self, word):
        """
        Returns if the word is in the data structure. A word could contain the dot character '.' to represent any one letter.
        """

        def dfs(word, root, idx):
            if idx == len(word):
                return root.end
            c = word[idx]
            if c == '.':
                for node in root.child:
                    if dfs(word, root.child[node], idx + 1):
                        return True
                return False
            else:
                if c in root.child:
                    return dfs(word, root.child[c], idx + 1)
                return False

        return dfs(word, self.root, 0)
# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)