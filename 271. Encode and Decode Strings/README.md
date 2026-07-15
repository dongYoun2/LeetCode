[Problem](https://leetcode.com/problems/encode-and-decode-strings/)



## Non-ASCII Delimter Encoding

Refer to the [07_15_2026.py](07_15_2026.py) file.


## Unicode Serialization Encoding

Refer to the [07_15_2026_unicode_serialization.py](07_15_2026_unicode_serialization.py) file.


## Length-Prefixed Encoding (Optimal)

The key point is to use a length of the word as a prefix, and use a delimiter (e.g. "#") to separate the length and the word. This idea is very similar to how data communication protocols, such as HTTP, encode data over the network.

[Submission](https://leetcode.com/problems/encode-and-decode-strings/submissions/2068978818/)—Runtime: 73 ms (beats 55.94%), Memory: 19.51 MB (beats 61.39%)

TC: $O(n)$, for both encode and decode, where $n$ is the total number of characters across all strings.
SC: $O(n)$, for both encode and decode.


```python
class Codec:
    def encode(self, strs: List[str]) -> str:
        """Encodes a list of strings to a single string.
        """
        encoded = []
        for word in strs:
            # Example: "Hello" -> "5#Hello"
            encoded.append(f"{len(word)}#{word}")

        return "".join(encoded)
        

    def decode(self, s: str) -> List[str]:
        """Decodes a single string to a list of strings.
        """
        print(s)
        decoded = []
        i = 0
        while i < len(s):
            # Find the separator after the length.
            j = i
            while s[j] != "#":
                j += 1

            length = int(s[i:j])

            # String starts after "#".
            start = j + 1
            end = start + length

            decoded.append(s[start:end])
            i = end

        return decoded


# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(strs))

```


cf.) The logic is the same as the [Approach 3: Chunked Transfer Encoding](https://leetcode.com/problems/encode-and-decode-strings/editorial/#approach-3-chunked-transfer-encoding) in the Editorial section.