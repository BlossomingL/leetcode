class TreeNode:
    def __init__(self):
        self.child = {} # 下一个字符
        self.is_end = False # 是否是最后一个字符


class Trie:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = TreeNode()

    def insert(self, word):
        """
        Inserts a word into the trie.
        """
        node = self.root
        for c in word:
            if c not in node.child:
                node.child[c] = TreeNode()
            node = node.child[c]
        node.is_end = True

    def search(self, word):
        """
        Returns if the word is in the trie.
        """
        node = self.root
        for c in word:
            if c not in node.child:
                return False
            node = node.child[c]
        return node.is_end

    def startsWith(self, prefix):
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        node = self.root
        for c in prefix:
            if c not in node.child:
                return False
            node = node.child[c]
        return True

# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)