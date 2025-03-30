# problem: https://leetcode.com/problems/minimum-genetic-mutation/
# submission: https://leetcode.com/problems/minimum-genetic-mutation/submissions/1591379122/

# 20 min
# Since there are only 4 characters and the gene length is fixed at 8, both time and space complexity are O(1). For the complexity analysis of the general case, where the gene string can have length 'n' and 'm' type of characters, please refer to the LeetCode Editorial section.

# cf.) I knew that I had to use BFS since I was solving BFS-related problems.


from collections import deque

class Solution:
    def minMutation(self, startGene: str, endGene: str, bank: List[str]) -> int:
        c_to_i = {'A': 0, 'C': 1, 'G': 2, 'T': 3}
        gene_chars = ['A', 'C', 'G', 'T']

        q = deque([startGene])
        cnt = 0
        visited = {startGene}

        while q:
            for _ in range(len(q)):
                curr_gene = q.popleft()
                if curr_gene == endGene:
                    return cnt

                for i in range(8):
                    c = curr_gene[i]
                    c_idx = c_to_i[c]

                    for j in range(1, 4):
                        nxt_c = gene_chars[(c_idx + j) % 4]
                        curr_l = list(curr_gene)
                        curr_l[i] = nxt_c
                        nxt_gene = "".join(curr_l)

                        if nxt_gene in bank and nxt_gene not in visited:
                            q.append(nxt_gene)
                            visited.add(nxt_gene)

            cnt += 1

        return -1
