# https://leetcode.com/problems/text-justification/description/

# took 41 min
# TC: O(n*m), where 'n' is the number of words and 'm' is the maxWidth
# SC: O(m) (output space is not considered)

# This is the second time I have solved this problem. I first did it on 02/24/2025, and I think it took around 1 hr then.

# This problem felt like a simulation problem. I think this kind of question is close to what you do in a real-world coding setting.

# There were several cases to consider.
# 1. addressing the last line
# 2. considering the line with only one word
# 3. how to distribute the proper size of spaces between words

class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        answer = []
        line_words = []


        def process_line(words):
            assert len(words) > 0

            total_space_len = maxWidth - len("".join(words))
            space_cnt = len(words) - 1

            line = words[0]

            if space_cnt == 0:
                line += " " * (maxWidth - len(line))
                return line

            base_space_len, surplus_space_cnt = divmod(total_space_len, space_cnt)

            for i in range(1, len(words)):
                line += " " * base_space_len
                if surplus_space_cnt:
                    line += " "
                    surplus_space_cnt -= 1

                line += words[i]

            return line


        for i, w in enumerate(words):
            line_words.append(w)
            line = " ".join(line_words)

            if len(line) > maxWidth:
                curr_w = line_words.pop()
                assert w == curr_w

                line = process_line(line_words)
                answer.append(line)

                line_words = [curr_w]


        # processing last line
        line = " ".join(line_words)
        line += " " * (maxWidth - len(line))

        answer.append(line)

        return answer

# notes while solving this problem

# n1 n2 n3

# 16 - 3 - 5 - 5

# word_cnt = 4
# blank_len = 10

# 10 // 3

# 10 divmod 3 => 3, 1
# 3+1 3 3

# 11 divmod 3 => 3, 2
# 3+1 3+1 3
