class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end_of_word = False

class WordDictionary:

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.is_end_of_word = True

    def search(self, word: str) -> bool:
        def dfs(node, i):
            if i == len(word):
                return node.is_end_of_word

            char = word[i]
            if char == ".":
                # Try all possible children
                return any(dfs(child, i + 1) for child in node.children.values())
            elif char in node.children:
                return dfs(node.children[char], i + 1)
            else:
                return False

        return dfs(self.root, 0)
