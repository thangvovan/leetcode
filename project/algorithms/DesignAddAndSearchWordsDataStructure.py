class TrieNode:
    def __init__(self):
        self.children = {}
        self.word = False

class WordDictionary:
    def __init__(self):
        self.root = TrieNode()      

    def addWord(self, word):
        current = self.root
        for character in word:
            current = current.children.setdefault(character, TrieNode())
        current.word = True
        
    def search(self, word):
        def dfs(node, index):
            if index == len(word):
                return node.word
            if word[index] == ".":
                for child in node.children.values():
                    if dfs(child, index+1):
                        return True
            if word[index] in node.children:
                return dfs(node.children[word[index]], index+1)
            return False
        return dfs(self.root, 0)