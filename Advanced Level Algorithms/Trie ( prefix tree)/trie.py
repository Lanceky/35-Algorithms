class TrieNode:
    def __init__(self):
        self.children = {}  # Maps characters to TrieNodes
        self.is_end_of_word = False

class Trie:
    def __init__(self):
        self.root = TrieNode()  # Empty root node

    def insert(self, word: str) -> None:
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.is_end_of_word = True

    def search(self, word: str) -> bool:
        node = self.root
        for char in word:
            if char not in node.children:
                return False
            node = node.children[char]
        return node.is_end_of_word

    def startsWith(self, prefix: str) -> bool:
        node = self.root
        for char in prefix:
            if char not in node.children:
                return False
            node = node.children[char]
        return True  # Prefix exists (doesn't need to be a complete word)