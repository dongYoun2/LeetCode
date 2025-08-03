[Problem](https://leetcode.com/problems/word-search-ii/description/)

I spent an hour and a half on this problem, but couldn't solve it.


## Trie-based DFS solution with backtracking

This approach is optimized solution for the `08_03_2025_trie_tle.py` solution. There are several changed points:
1. `TrieNode` class doesn't contain current `letter` character (value). Also, `is_end` boolean is changed to `word` string, which stores the full word at the terminal node.
2. The Trie traversal is done within the `dfs()` function instead of separate methods defined in the `Trie` class from `08_03_2025_trie_tle.py`. This avoids repeated traversals.
3. Mark visited cells with `'#'` character on the board, which is simply a in-place modification for backtracking.
4. Dynamic leaf node pruning technique is applied to the Trie which significantly reduces execution time in practice. ([submission without this pruning](https://leetcode.com/problems/word-search-ii/submissions/1722367279/) takes 4639 ms to run.)
    ```python
    # dynamic leaf node pruning part from the full code below
    if not child.children and child.word is None:
        node.children.pop(ch)
    ```

    To further explain the 4th point, this technique is beneficial since when we find a word (`child.word`), we do `child.word = None` (see the code below) so we don’t report it again. After that, if that `node` (not the `child`, which is equivalent to `node.children[ch]`) has no descendants (no other words branch below it), then that entire branch of the trie is useless moving forward. By doing `node.children.pop(ch)`, we remove that dead branch so future DFS steps encountering the same prefix will fail earlier—saving work. **It incrementally shrinks the trie as words are found.** (**Notice that dictionary `pop()` method is performed on the `node.children`, not the `child` node itself.** I was confused because of this at first.)

<br>

Notations for complexity analysis:
- $m$: number of rows in the board
- $n$: number of columns in the board
- $W$: number of words in the input list
- $L$: average/maximum length of the words
- Branching factor is 4 for simplicity. (technically 3, since we cannot go back to the previous cell)

<br>

- [Submission](https://leetcode.com/problems/word-search-ii/submissions/1722367406/) (Runtime: 547 ms, Memory: 19.2 MB)
- TC: $O(m * n * 4^L)$. $4^L$ is for the DFS traversal for each cell.
- SC: $O(W*L+ L)$ -> $O(W*L)$. Trie construction + recursion stack. (Output array is not counted)

<br>

```python
class TrieNode:
    def __init__(self):
        self.children = {}
        self.word = None  # store full word at terminal

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        # build trie
        root = TrieNode()
        for w in words:
            node = root
            for ch in w:
                if ch not in node.children:
                    node.children[ch] = TrieNode()
                node = node.children[ch]
            node.word = w  # mark end

        m, n = len(board), len(board[0])
        res = []

        def dfs(r, c, node):
            ch = board[r][c]
            if ch not in node.children:
                return
            child = node.children[ch]
            # found a word
            if child.word:
                res.append(child.word)
                child.word = None  # avoid duplicate

            # mark visited
            board[r][c] = '#'
            for dr, dc in ((1,0),(-1,0),(0,1),(0,-1)):
                nr, nc = r + dr, c + dc
                if 0 <= nr < m and 0 <= nc < n and board[nr][nc] != '#':
                    dfs(nr, nc, child)
            board[r][c] = ch  # restore

            # prune leaf
            if not child.children and child.word is None:
                node.children.pop(ch)


        for i in range(m):
            for j in range(n):
                dfs(i, j, root)

        return res

```