# problem: https://leetcode.com/problems/longest-repeating-character-replacement/
# spent around half an hour, but couldn't solve it.


# this is a sliding window problem.

# my initial approach was for each character, pick one, and find the longest substring that can be formed with that character by changing other characters k times. Then, return the longest one among all characters (the number of english characters is 26; constant). Then, how can we find the longest substring for a given character? i thought of translating into the interval problem. so each interval contains a start and end index of the consecutive string of that given character. but, i was stuck there.

# then, i thought of using a sliding window technique. i initialized the window size to k, and trying to thinkg of how to find the longest substring. however, the correct and optimal solution is starting from the window size of 1, and expanding the window size based on the maximum frequency of the characters in the window we have seen so far. for details, refer to the README.md file.

# cf.) this problem is similar to "3. Longest Substring Without Repeating Characters" problem. i was able to solve that problem maybe because i selected the problem based on the algortihm category. i think it's a good time to practice and focus on sliding window problems.


class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        pass