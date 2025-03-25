# https://leetcode.com/problems/longest-string-chain/

# 40 min
# TC: O(N*log N + N^2*L) -> O(N^2*L), where N is the number of words and L is the maximum word length. (N*log N for sorting, and L for predecessor checking with two-pointer algorithm.) However, time complexity can be further optmized to O(N*L^2); see the explanation in the markdown file.
# SC: O(N) (hash table)

# As soon as I saw this question, I felt it was a dynamic programming problem, so I assumed it so. Since the maximum number of words is 1K from the constraint, I assumed that the time complexity has to be similar to O(N^2).

# I also thought maybe this was a topological sorting problem (In my notes, I was trying to see if topological sorting works). I assumed that checking only the nodes (words) in the last level was sufficient. However, I realized that there can be a word chain with the current word constructed on top of the node (word) from the previous levels.

# Turning back to the DP algorithm, I found out that the word chain for the current word can be constructed by adding this word to any word chain with the last word's length as the `len(current_word) - 1` (Need to check only these words). Therefore, this can be stored in a hash map where the "key" is the word length, and the "value" is the tuple of 1) the word itself and 2) the maximum length of the word chain.

# To check whether the potential predecessors (all previous words with length len(current_word) - 1) are actual predecessors of the current word, I used a two-pointer algorithm, which has a time complexity of O(L). In this setting, by keeping track of the maximum length of the word chain, the answer could be found.

# However, this solution is suboptimal when there exist many words of the same length. In this case, the hasp map is skewed — leading to the worst-case time complexity, O(N^2*L).


from collections import defaultdict

class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        words = sorted(words, key=lambda w: len(w))

        h_map = defaultdict(list)
        h_map[len(words[0])].append((words[0], 1))


        def is_predecessor(w1, w2):
            assert len(w1) + 1 == len(w2)

            idx1 = idx2 = 0
            is_pred = False
            while idx1 < len(w1):
                if w1[idx1] == w2[idx2]:
                    idx1 += 1
                    idx2 += 1
                elif not is_pred:
                    is_pred = True
                    idx2 += 1
                else:
                    is_pred = False
                    break

            if idx1 == len(w1) and idx2 == len(w2) - 1:  # character is inserted in the last position
                is_pred = True

            return is_pred


        global_max_chain_len = 1
        for i in range(1, len(words)):
            w_len = len(words[i])
            pred_len = w_len - 1

            max_chain_len = 1
            for pred_w, prev_chain_len in h_map[pred_len]:
                if is_predecessor(pred_w, words[i]):
                    max_chain_len = max(max_chain_len, prev_chain_len + 1)

            h_map[w_len].append((words[i], max_chain_len))
            global_max_chain_len = max(global_max_chain_len, max_chain_len)

        return global_max_chain_len

# notes while solving the problem

# a ab k acd aced acefd
# a ab k acd aced acdt  acdqt

# a -> ab
#   -> acd -> aced
#          -> acdt -> acdqt
# k

# a b ba bca bda bdca
# 1 1 2
