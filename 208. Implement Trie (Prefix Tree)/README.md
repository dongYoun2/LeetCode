[Problem](https://leetcode.com/problems/implement-trie-prefix-tree/description/)

## Trie Implementation using `defaultdict`

The code below is based on the `09_02_2025.py`, optimizing the three points listed in the comments in that file.


- [Submission](https://leetcode.com/problems/implement-trie-prefix-tree/submissions/1757563497/)
- TC: $O(n)$ for insert, search, and startsWith, where n is the length of the input (either `word` or `prefix`).
- SC: $O(\bigl(m \cdot \mathbb{E}[n]\bigr)$, where $m$ is the number of words inserted and $\mathbb{E}[n]$ is the average length of the words (space complexity for the entire Trie data structure).
<br>

```python
from collections import defaultdict
from typing import Optional


class Node:
    def __init__(self, val=None):
        self.children = defaultdict(Node)
        self.is_end = False


class Trie:

    def __init__(self):
        self.root = Node()


    def insert(self, word: str) -> None:
        curr = self.root
        for c in word:
            curr = curr.children[c]

        curr.is_end = True


    def _starts_with_node(self, prefix: str) -> Optional[Node]:
        curr = self.root
        for c in prefix:
            if c not in curr.children:
                return None

            curr = curr.children[c]

        return curr


    def search(self, word: str) -> bool:
        find = self._starts_with_node(word)

        return bool(find) and find.is_end


    def startsWith(self, prefix: str) -> bool:
        return bool(self._starts_with_node(prefix))


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)

```