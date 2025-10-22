# submission: https://leetcode.com/problems/design-add-and-search-words-data-structure/submissions/1808614553/
# runtime: 1386 ms, memory: 67.99 MB

# 30 min
# refer to the 05_16_2025.py for the time and space complexity analysis.

# pretty straightforward to implement using trie and dfs traversal. however, spent some time debugging, but realized that first i didn't call the `dfs` function in the `search` method, then again, find out that i didn't put the `return` before the dfs() function call.. lol

# saerch method can be slightly optimized by:
# 1. pasing index to the `dfs` function instead of slicing the string.
# 2. iteratively traverse the trie when the character is not a wildcard. This allows for avoiding extra recursion stack frames.
# the improved code can be found at: https://leetcode.com/problems/design-add-and-search-words-data-structure/submissions/1808631470/ (runtime: 1204 ms, memory: 68.0 MB)


class TrieNode:
    def __init__(self, ch: str = None, is_terminated: bool = False):
        self.val = ch
        self.children = {}
        self.is_terminated = is_terminated


class WordDictionary:

    def __init__(self):
        self.trie = TrieNode()


    def addWord(self, word: str) -> None:
        curr = self.trie
        for ch in word:
            if ch not in curr.children:
                curr.children[ch] = TrieNode(ch)
            curr = curr.children[ch]
        curr.is_terminated = True


    def search(self, word: str) -> bool:
        def dfs(word, curr: TrieNode):
            if word == '':
                return curr.is_terminated

            ch = word[0]
            if ch == '.':
                for child in curr.children.values():
                    if dfs(word[1:], child):
                        return True
                return False
            elif ch not in curr.children:
                return False

            return dfs(word[1:], curr.children[ch])


        return dfs(word, self.trie)


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)
