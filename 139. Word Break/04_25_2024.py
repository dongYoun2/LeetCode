# submission: https://leetcode.com/problems/word-break/submissions/1591554313/
# runtime: 2 ms (Beats 74.30%), memory: 18.11 MB (Beats 49.68%)
# idk the time spent

# symbols:
# n: the number of characters in the string `s`
# m: the number of words in the wordDict
# k: the average length of words in the wordDict

# TC: O(n^2*m*k)
# - memoization (`checked` set) ensures each suffix of `s` is processed only once.
# - number of possible suffixes is at most n; for each suffix, we loop over m words and prefix check (`w in s` and `s.index(w) == 0`) costs O(k).
# - due to the python string slice, overall TC is O(n^2*m*k) (with index-based approach or other languages, it would be O(n*m*k)).

# SC: O(n^2)
# - recursion stack O(n) and `checked` set O(n)
# - likewise, due to the python string slice, overall SC is O(n^2) (with index-based approach or other languages, it would be O(n)).


# i came up with dfs + backtracking approach. however, i didn't use memoization technique (no `checked` set), so it failed on the case where the same suffix is checked multiple times (failed submission: https://leetcode.com/problems/word-break/submissions/1241520580/). realizing this, i added the `checked` set to cache the negative suffixes to avoid redundant checks.


# cf.) instead of using `w in s and s.index(w) == 0` for the prefix check, we can simply use `s.startswith(w)`. moreover, the code can be improved with index-based approach instead of string slicing.


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        def dfs(self, s, checked):
            if s == "":
                return True

            if s in checked:
                return False
            
            checked.add(s)
            
            for w in wordDict:
                if w in s and s.index(w) == 0 and dfs(self, s[len(w):], checked):
                    return True
            
            return False

        return dfs(self, s, set())
