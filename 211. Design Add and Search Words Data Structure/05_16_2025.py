# submission: https://leetcode.com/problems/design-add-and-search-words-data-structure/submissions/1636825205/
# runtime: 1405 ms, memory: 52.6 MB

# 44 min
# TC:
# - addWord: O(L), where L is the length of the `word`
# - search: O((L-k)*d^k) -> O(L*d^k) -> O(L), where k (<=2) is the number of "." (wildcards) in a search string and d (=26, size of the lowercase‐English alphabet) is the dimension of alphabets in a trie. Since k is negligible and d is fixed in this problem, we can regard both as constants.
# SC:
# - addWord:
#   - Auxiliary (transient): O(1)
#   - Structural (persistent): O(L) (up to one new node per character)
# - search:
#   - Auxiliary: O(L) (recursion stack space)
#   - Structural: O(0) (does not modify the trie)
# - Space complexity for the entire trie is O(N * L_mean), where N is the number of insertions, and L_mean is the average length of inserted words.


# From LeetCode Top Interview 150 - Trie


# Although I knew which data structure to use beforehand, it's important to note that this problem is a trie problem since there will be many string insertions and searches. Using Trie in this case significantly reduces the time complexity of the search operation to O(L), whereas the brute-force solution would take O(N * L_mean) time complexity.

# I vaguely remembered the trie data structure and had to figure it out from scratch. When solving "208. Implement Trie (Prefix Tree)" two months ago, I looked up the Trie Wikipedia page linked in the question and defined the TrieNode. I couldn't remember the details, so I used a dictionary to represent the trie this time, which makes the code not clean—e.g., using "end" key to indicate the terminal flag of a word (but the Editorial code also simply uses a dictionary and using '$' for the terminal flag.) Note that this termnial flag is essential for the trie data structure to work properly (My first two submissions failed since I forgot to add this flag).

# Another difference between this problem and "208. Implement Trie (Prefix Tree)" is that we need to use DFS to handle the wildcard character. The search function is a recursive function that traverses the tree. If the current character is a wildcard, we need to check all possible paths in the tree.

# Moreover, the code below can be further improved by:
# 1. Using a TrieNode class to represent the trie node instead of a dictionary. (for better readability, maintainability, and abstraction)
# 2. Using a simple for-loop when the character is not a wildcard during the search. This allows for avoiding extra recursion stack frames. (For more details, refer to the Editorial code.)


class WordDictionary:

    def __init__(self):
        self.trie = {}


    def addWord(self, word: str) -> None:
        curr = self.trie
        for c in word:
            if c not in curr:
                curr[c] = {}

            curr = curr[c]

        curr['end'] = True  # to indicate the end of the word

    def search(self, word: str) -> bool:
        return self.helper_search(word, self.trie)


    def helper_search(self, word, node):
        if len(word) == 0:
             return 'end' in node

        if word[0] == ".":
            ret = False
            for c in node:
                if c == 'end': continue

                if self.helper_search(word[1:], node[c]):
                    ret = True

            return ret

        first_letter = word[0]
        if first_letter in node:
            return self.helper_search(word[1:], node[word[0]])
        else:
            return False


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)
