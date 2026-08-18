class Node:
    def __init__(self, val = ""):
        self.val = val
        self.children = {}

    def insert(self, child):
        if child not in self.children:
            self.children[child] = Node(child)
        return self.children[child]

    def search(self, word):
        if len(word) == 0:
            return self.children
        w = word[0]
        if w in self.children:
            return self.children[w].search(word[1:])
        return None

class Trie:
    def __init__(self):
        self.root = Node()

    def insert(self, word: str) -> None:
        node = self.root
        for w in word:
            node = node.insert(w)
        node.insert("\0")

    def search(self, word: str) -> bool:
        node = self.root.search(word)
        return False if node == None else False if "\0" not in node else True

    def startsWith(self, prefix: str) -> bool:
        return self.root.search(prefix) != None