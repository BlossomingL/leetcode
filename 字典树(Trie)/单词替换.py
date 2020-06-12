class Solution:
    def __init__(self):
        self.root = {}
        self.end_flag = '#'

    def replaceWords(self, dict, sentence):
        for word in dict:
            node = self.root
            for c in word:
                if c not in node:
                    node[c] = {}
                node = node[c]
            node[self.end_flag] = True

        def get_replace_root(word):
            node = self.root
            res = []
            for c in word:
                res.append(c)
                if c not in node:
                    return False
                node = node[c]
                if self.end_flag in node:
                    return ''.join(res)
            return False

        res = []
        for word in sentence.split():
            re = get_replace_root(word)
            if re == False:
                res.append(word)
            else:
                res.append(re)
        return ' '.join(res)
