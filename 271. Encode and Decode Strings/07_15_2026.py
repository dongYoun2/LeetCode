# submission: https://leetcode.com/problems/encode-and-decode-strings/submissions/2068755105/
# runtime: 72 ms (beats 60.61%), memory: 19.43 MB (beats 85.76%)
# 6 ms
# solved with non-ascii delimter encoding

# let n be the total number of characters across all strings
# TC: O(n), for both encode and decode
# SC: O(n), for both encode and decode


# we can see that only 256 valid ascii characters are used in the input strings. therefore, i simply considered using a non-ascii character as a delimiter to encode and decode strings. however, as asked in the follow up question, the intended solution also allows for non-ascii characters, which require generalized algorithms for this problem.


class Codec:
    def encode(self, strs: List[str]) -> str:
        """Encodes a list of strings to a single string.
        """
        return "ㅁ".join(strs)


    def decode(self, s: str) -> List[str]:
        """Decodes a single string to a list of strings.
        """
        return s.split("ㅁ")


# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(strs))
