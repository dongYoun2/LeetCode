# submission: https://leetcode.com/problems/implement-trie-prefix-tree/submissions/1757543034
# runtime: 47 ms, memory: 32.7 MB

# 21 min
# TC: O(n) for insert, search, and startsWith, where n is the length of the input (either 'word' or 'prefix')
# SC: O(m*E[n]) where m is the number of words inserted and E[n] is the average length of the words (space complexity for the entire Trie data structure)


# From LeetCode Top Interview 150 - Trie


# this is a Trie data structure implementation problem. this is the third time solving this, and finally i could implement it without consulting the Trie wikipedia provided from the problem description.

# however, few improvements can be made:
# 1. default value for the `is_end` parameter in Node (or TrieNode) class can be `False`, or simply `self.is_end = False` can be set in the constructor to make it more encapsulated.
# 2. no need of `self.val` since the trie key, character, and the value is the same in this case. (key == value)
# 3. using defaultdict for `children` instead of a pure dictionary. this allows the code to be simpler by removing existence checks in the `children` (`c in curr.children`)

# refer to the markdown file for the optimized version.


from typing import Optional


class Node:
    def __init__(self, val=None, is_end=True):
        self.val = val
        self.children = {}
        self.is_end = is_end


class Trie:

    def __init__(self):
        self.root = Node()


    def insert(self, word: str) -> None:
        curr = self.root

        for c in word:
            if c not in curr.children:
                curr.children[c] = Node(c, is_end=False)

            curr = curr.children[c]

        curr.is_end = True


    def _starts_with_node(self, prefix: str) -> Optional[Node]:
        curr = self.root

        for c in prefix:
            if c in curr.children:
                curr = curr.children[c]
            else:
                return None

        return curr


    def search(self, word: str) -> bool:
        final_node = self._starts_with_node(word)

        return bool(final_node) and final_node.is_end


    def startsWith(self, prefix: str) -> bool:
        return bool(self._starts_with_node(prefix))


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
