# KMP Algorithm

LeetCode [28. Find the Index of the First Occurence in a String](https://leetcode.com/problems/find-the-index-of-the-first-occurrence-in-a-string/description/) can be solved using the KMP (Knuth-Morris-Pratt) algorithm.

The core idea of this algorithm is to avoid redundant comparisons when searching for a pattern in a text by using previous match information to skip some characters without rechecking them. This makes the time complexity as **O(n+m)**, where `n` is the length of text to search on, and `m` is the length of pattern.

In KMP algorithm, most important step is to construct an **LPS (longest prefix suffix) array**. The array at index `i` (`lps[i]`) stores the length of longest **proper prefix** that is also a **suffix** of the substring that ends at that index (`lps[0...i]`).
- **proper prefix**: all prefix excluding word itself is a proper prefix of that word.


**Example: LPS Array Construction for "ABABAC"**

| i   | pattern[i] | pattern[0...i] | Longest proper prefix == suffix | lps[i] |
| --- | ---------- | -------------- | ------------------------------- | ------ |
| 0   | A          | A              | – (no proper prefix/suffix)     | 0      |
| 1   | B          | AB             | –                               | 0      |
| 2   | A          | ABA            | A                               | 1      |
| 3   | B          | ABAB           | AB                              | 2      |
| 4   | A          | ABABA          | ABA                             | 3      |
| 5   | C          | ABABAC         | – (no match)                    | 0      |

So, the LPS array is: `[0, 0, 1, 2, 3, 0]`

Easy way to think of constructing LPS array is for each `pattern[0...i]`, we can find the longest proper prefix that is also a suffix.Time complexity for this approach is $O(m^2)$. However, this can be optimized to O(m), which has the benefit of making the entire search algoritm as **O(n+m)**.

After constructing LPS array, it can be used to avoid redundant comparisons. More concretely, whenever text and pattern mismatch occurs at text index `i` and pattern index `j`, we can continue comparing starting from `pattern[lps[j-1]]` with `text[i]`. More detailed explanation and implementation can be found in [GeeksforGeeks KMP Algorithm for Pattern Searching](https://www.geeksforgeeks.org/kmp-algorithm-for-pattern-searching/).