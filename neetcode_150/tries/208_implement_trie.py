class TrieNode:
    def __init__(self, ch):
        self.char = ch
        self.children = {}
        self.is_complete = False
class Trie:

    def __init__(self):
        self.root = TrieNode('*')

    def insert(self, word: str) -> None:
        cur = self.root

        for c in word:
            if c not in cur.children:
                new_node = TrieNode(c)
                cur.children[c] = new_node
            cur = cur.children[c]

        cur.is_complete = True

    def search(self, word: str) -> bool:
        cur = self.root

        for c in word:
            if c not in cur.children:
                return False
            cur = cur.children[c]

        return cur.is_complete
    def startsWith(self, prefix: str) -> bool:
        cur = self.root

        for c in prefix:
            if c not in cur.children:
                return False
            cur = cur.children[c]

        return True