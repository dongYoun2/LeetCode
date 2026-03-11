# submission: https://leetcode.com/problems/design-add-and-search-words-data-structure/submissions/1945273854/
# runtime: 997 ms (beats 43.10%), memory: 69.04 MB (beats 17.36%)
# 25 min

# time and space complexities are the same as 05_16_2025.py. refer to it for details.


# this problem can be solved with a trie data structure and dfs traversal. the code below is pretty straightforward.


class TrieNode:
    def __init__(self, value=None, is_terminal=False):
        self.value = value
        self.children = {}
        self.is_terminal = is_terminal

class WordDictionary:

    def __init__(self):
        self.trie = TrieNode(None, is_terminal=True)
        

    def addWord(self, word: str) -> None:
        curr = self.trie
        for c in word:
            if c not in curr.children:
                curr.children[c] = TrieNode(c)
            curr = curr.children[c]
        
        curr.is_terminal = True
        

    def search(self, word: str) -> bool:
        def search_helper(node, idx: int) -> bool:
            if idx >= len(word):
                return node.is_terminal

            c = word[idx]
            if c == ".":
                for child in node.children.values():
                    if search_helper(child, idx + 1):
                        return True

            if c not in node.children:
                return False
            
            return search_helper(node.children[c], idx + 1)


        return search_helper(self.trie, 0)
    

# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)