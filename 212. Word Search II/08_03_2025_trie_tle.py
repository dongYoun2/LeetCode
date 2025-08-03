# submission: https://leetcode.com/problems/word-search-ii/submissions/1722331956/
# Time Limit Exceeded

# Refer to the markdown file for the variable notations.

# TC: O(m * n * 4^L * L), last L is for the python slicing.
# SC: O(W*L + L + L^2) -> O(W*L + L^2). trie construction + recursion stack + slicing considering the recursion.

# From LeetCode Top Interview 150 - Trie

# I attempted solving using a Trie-based DFS, which the problem is intended for. I simply defined Trie class, which I learned from previous Trie problems (208. Implement Trie (Prefix Tree) and 211. Design Add and Search Words Data Structure).

# if I simply implement like that however, it's inefficient since there would be repeated traversals on the Trie. You can easily see that there are consecutive trie's has_prefix() and search() method calls in the dfs() function, which both travers the Trie from the root. Thus, I get the TLE again.

# This problem is solved in the code described in the markdown file. please refer to that for more details.


class TrieNode:

    def __init__(self, letter=None, is_end=False):
        self.letter = letter
        self.is_end = is_end
        self.children = {}


class Trie:

    def __init__(self):
        self.root = TrieNode()


    def insert(self, word):
        curr = self.root

        for c in word:
            if c not in curr.children:
                curr.children[c] = TrieNode(c)

            curr = curr.children[c]

        curr.is_end = True


    def get_prefix_node(self, prefix):
        curr = self.root

        for c in prefix:
            if c not in curr.children:
                return None

            curr = curr.children[c]

        return curr


    def has_prefix(self, prefix):
        return bool(self.get_prefix_node(prefix))


    def search(self, word):
        node = self.get_prefix_node(word)
        return bool(node) and node.is_end


class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        m, n = len(board), len(board[0])

        dys = [-1, 0, 1, 0]
        dxs = [0, 1, 0, -1]

        is_valid = lambda r, c: 0 <= r < m and 0 <= c < n


        def dfs(y, x, curr_str):
            curr_str += board[y][x]

            if not trie.has_prefix(curr_str):
                return

            if trie.search(curr_str):
                ans.add(curr_str)

            for dy, dx in zip(dys, dxs):
                next_y, next_x = y + dy, x + dx

                if is_valid(next_y, next_x) and (next_y, next_x) not in visited:
                    visited.add((next_y, next_x))
                    dfs(next_y, next_x, curr_str)
                    visited.remove((next_y, next_x))



        # add words to trie
        trie = Trie()
        for word in words:
            trie.insert(word)

        ans = set()

        # dfs on board
        visited = set()
        for i in range(m):
            for j in range(n):
                visited.add((i, j))
                dfs(i, j, "")
                visited.remove((i, j))

        return list(ans)
