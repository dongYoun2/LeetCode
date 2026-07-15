# submission: https://leetcode.com/problems/encode-and-decode-strings/submissions/2068736743/
# runtime: 166 ms (beats 7.30%), memory: 19.59 MB (beats 61.39%)
# 23 min (include "07_15_2026.py" time)
# solved with unicode serialization encoding (this approach also solves the follow up question since `ord()` converts characters to unicode values, though it's not optimal)

# symbols:
# - n: total number of characters across all strings
# - k: digits per character code

# TC: O(nk), for both encode and decode
# SC: O(nk), for both encode and decode


# after solving with the "07_15_2026.py" approach, i assumed that is not the intended solution. so, while brainstorming for other approaches, i came up with the idea of coverting each character to its unicode integer value, then use two delimiters "#" and "_" to distinguish between each unicode value and each string (word), respectively. however, the runtime is not optimal in practice since each character is converted to 3-4x more characters, including "#" delimter. for an optimal solution, refer to the README.md.

# cf.) i didn't look at the follow up question while writing this solution.


class Codec:
    def encode(self, strs: List[str]) -> str:
        """Encodes a list of strings to a single string.
        """
        enc_words = ["#".join([str(ord(c)) for c in word]) for word in strs]

        return "_".join(enc_words)


    def decode(self, s: str) -> List[str]:
        """Decodes a single string to a list of strings.
        """
        decoded_strs = ["".join([chr(int(c)) for c in word.split("#")]) if word else "" for word in s.split("_")]
        
        return decoded_strs


# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(strs))
