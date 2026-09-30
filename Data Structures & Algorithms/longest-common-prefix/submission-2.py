class TrieNode:
    def __init__(self):
        self.children = {}
        self.end_of_word = False

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str):
        node = self.root
        for c in word:
            if c not in node.children:
                node.children[c] = TrieNode()
            
            node = node.children[c]
        node.end_of_word = True
    
    def longest_common_prefix(self):
        res = []
        node = self.root

        while len(node.children) == 1:
            if node.end_of_word:
                break
            key = list(node.children.keys())[0]
            res.append(key)
            node = node.children[key]
        
        return "".join(res)

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        trie = Trie()
        for word in strs:
            trie.insert(word)
        
        return trie.longest_common_prefix()