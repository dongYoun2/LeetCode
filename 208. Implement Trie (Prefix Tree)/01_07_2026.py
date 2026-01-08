# submission: https://leetcode.com/problems/implement-trie-prefix-tree/submissions/1878222321/
# runtime: 43 ms, memory: 34.08 MB

# 20 min
# refer to the README.md for the complexity analysis.


# Now, I feel pretty comfortable with implementing the Trie data structure from scratch.


from typing import Optional

class TrieNode:
    def __init__(self, val=None):
        self.val = val
        self.children = {}
        self.is_terminated = False


class Trie:

    def __init__(self):
        self.root = TrieNode()
        

    def insert(self, word: str) -> None:
        assert len(word) >= 1
        curr = self.root
        for c in word:
            child = curr.children.setdefault(c, TrieNode(c))
            curr = child
        curr.is_terminated = True
        

    def _find_node(self, string: str) -> Optional[TrieNode]:
        assert len(string) >= 1
        curr = self.root
        for c in string:
            if c in curr.children:
                curr = curr.children[c]
            else:
                return None
        
        return curr


    def search(self, word: str) -> bool:
        assert len(word) >= 1
        target_node = self._find_node(word)
        return False if target_node is None else target_node.is_terminated == True
        

    def startsWith(self, prefix: str) -> bool:
        assert len(prefix) >= 1
        target_node = self._find_node(prefix)
        return False if target_node is None else True
        


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
