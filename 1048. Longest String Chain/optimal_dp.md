## Fully Optimized Version

`03_24_2025.py` ($O(N^2 L)$) can be further optimized to time complexity of $O(N L^2)$. When there are many words with the same length, `03_24_2025.py` might have to loop through all of the previous words, leading to $O(N)$ time complexity. This is because the DP hash table stores the **word length** as the key. Instead, the table can directly store the **word** itself as the key and loop over all predecessors by removing each character of the current word (Notice that we can directly find the true predecessors based on the current word and check if each predecessor has been already stored in the hash table.). The time complexity of this process is $O(L)$ and makes the overall time complexity $O(N L^2)$. This can be solved by either a bottom-up or top-down approach.

##### DP Bottom-up
- Notice that we have to sort by word length beforehand.

```python
class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        words = sorted(words, key=lambda w: len(w))

        dp_dict = {}    # memoization
        global_max_chain_len = 1

        for word in words:
            max_chain_len = 1
            for j in range(len(word)):
                predecessor = word[:j] + word[j+1:]

                cached_len = dp_dict.get(predecessor, 0)
                max_chain_len = max(max_chain_len, cached_len + 1)

            dp_dict[word] = max_chain_len
            global_max_chain_len = max(global_max_chain_len, max_chain_len)

        return global_max_chain_len

```


##### DP Top-down
- Notice that we have to check whether the current word is present in the whole array every time we perform `dfs()`.
```python
class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        dp_dict = {}    # memoization
        all_words = set(words)

        def dfs(word):
            if word in dp_dict:
                return dp_dict[word]

            max_chain_len = 1
            for i in range(len(word)):
                predecessor = word[:i] + word[i+1:]

                if predecessor in all_words:
                    cached_len = dfs(predecessor)
                    max_chain_len = max(max_chain_len, cached_len + 1)

            dp_dict[word] = max_chain_len

            return max_chain_len


        return max(dfs(w) for w in words)
```