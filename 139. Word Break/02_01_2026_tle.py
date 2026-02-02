# submission: https://leetcode.com/problems/word-break/submissions/1904848271/
# time limit exceeded
# 45 min


# i started thinking of first looping over words in the `wordDict` and trying to match the word with the prefix of the string `s`. this approach is equivalent to the "04_25_2024.py" solution. 

# realizing that there would be repeated word checks, i built the trie for efficient checks. 

# however, this submission got TLE on the specific test case. i couldn't figure out why, and with the help of chatGPT, i noticed that it's due to the absence of memoization in dfs. the same approach with memoization code (succeeded submission) can be found here: https://leetcode.com/problems/word-break/submissions/1904848348/. the only difference is the `lru_cache` decorator on the `dfs` function.

# though the time complexity big O notation is the same as the "04_25_2024.py" solution (prefix check in for loop on `wordDict` version), trie helps when `wordDict` is large. additionally, trie optimization shines when it's used on the DP approach. for more details, refer to the Editorial section's Approach 3 "Bottom-Up Dynamic Programming" and Approach 4 "Trie Optimization".

# cf.) the code can be further improved with index-based approach instead of string slicing. also, note that this problem can be solved with BFS. when solving either with DFS or BFS, the key is that vertex is each index (in the index-based approach) and edge between node i and j is whether the substring from i to j is in the `wordDict` (in other words, whether s[:j+1] can be built, assumming the previous substrings are already built). lastly, the best approach for this problem would be DP with trie optimization.


class TrieNode:
    def __init__(self, val, is_terminal=False):
        self.val = val
        self.children = {}
        self.is_terminal = is_terminal


class Trie:
    def __init__(self):
        self.root = TrieNode(-1)

    def insert(self, word):
        curr = self.root
        for c in word:
            child = curr.children.setdefault(c, TrieNode(c))
            curr = child
        
        curr.is_terminal = True


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        trie = Trie()
        for word in wordDict:
            trie.insert(word)
        

        def dfs(remain_s):
            if remain_s == '':
                return True

            curr_chars = []
            curr = trie.root
            for c in remain_s:
                if c not in curr.children:
                    return False

                curr_chars.append(c)

                if curr.children[c].is_terminal:
                    curr_word = ''.join(curr_chars)
                    assert remain_s[:len(curr_word)] == curr_word
                    if dfs(remain_s[len(curr_word):]):
                        return True

                curr = curr.children[c]
            
            return False


        return dfs(s)


# notes while solving:
# trie + dfs
