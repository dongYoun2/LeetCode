# submission: https://leetcode.com/problems/word-ladder/submissions/1651106936/
# runtime: 3317, memory: 20.65 MB

# 43 min

# TC: O(N*L + N*26*L^2) -> O(N*L^2), where N is the number of words in the `wordList` and L is the length of the word.
# - O(N*L): For constructing a hash table for `wordList`
# - O(N): In the worst case, all words in the `wordList` will be enqueued exactly once.
# - O(26*L^2): For each dequeued node, we perform the nested loop logic shown in the below code. (26 is the number of English characters)

# SC: O(2*N*L + N*L) -> O(N*L)
# - O(2*N*L): `wordList` and `visited` set (or hash table)
# - O(N*L): In the worst case, the queue can hold up to O(N) words at once (each a length-L string plus one integer)


# From LeetCode Top Interview 150 - Graph BFS

# To be honest, I don't think I would be able to solve this problem if I didn't know this is a Graph BFS problem. Since we never know which data structure and algorithm to use in coding interviews, I would better understand why the hash table plus BFS approach is most reasonable here.

# Cues to detect this problem as a Graph BFS problem:
# Whenever we see a problem that asks for a “shortest sequence” of small, discrete steps (here, changing one letter at a time), that should immediately suggest “shortest‐path on an implicit graph.” Concretely:
# 1. Recognize the “shortest transformation” = “shortest path in an unweighted graph.”
# 2. Realize that the graph is implicit (words are nodes; one‐letter difference = edge).
# 3. To perform BFS, we need to be able to enumerate neighbors quickly—hence, keep the dictionary in a hash structure (either a set of words or a map from wildcard patterns to words).

# cf.) There are two optimized solutions for this problem, which are explained in the LeetCode Editorial section. Although the asymtotic time complexity is the same (the space complexity of both optimized solutions is O(N*L^2), but unless L is too large or RAM is very limited, optimized versions are better in practice), they are faster in practice since they never loop over all 26 letters at each position; instead, they only process actual neighbors once. For more details, refer to the Editorial section.


from collections import deque

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        assert beginWord != endWord

        L = len(beginWord)
        visited = set()
        word_set = set(wordList)

        if endWord not in word_set:
            return 0

        letters = 'abcdefghijklmnopqrstuvwxyz'

        ans = 1
        q = deque([(beginWord, -1)])    # (word, prev_changed_pos)

        while q:
            for _ in range(len(q)):
                curr_word, prev_changed_pos = q.popleft()
                visited.add(curr_word)

                for i in range(L):
                    if i == prev_changed_pos:   # skip previously changed index
                        continue

                    for c in letters:
                        if c == curr_word[i]:   # skip curr_word
                            continue

                        adj_word = curr_word[:i] + c + curr_word[i+1:]
                        if adj_word == endWord:
                            return ans + 1

                        if adj_word not in visited and adj_word in word_set:
                            q.append((adj_word, i))

            ans += 1

        return 0


# notes while solving:
# hit

# fit 0    hot 1                        git 0    hif 2

#          dot 0     lot 0

#          dog 2     log 2
