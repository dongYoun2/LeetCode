# submission: https://leetcode.com/problems/accounts-merge/submissions/1779279626/
# wrong solution

# this is my first attempt. i thought it's a hash table problem, so i simply used a hash table (name -> email sets) to store the accounts. however, it fails on the specific test case (can check in the submission link).

# the problem with this code is that it only merges an account into the first matching set it finds. if there are multiple sets that contain the same email, it only merges the account into the first one. In words, it does not handle transitive merges across multiple sets.

# this is why the correct approach for this problem is using either 1) DFS on graph or 2) union find (Disjoint Set Union). for more details, refer to the README.md file.


class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        acc_table = {}

        for acc in accounts:
            name = acc[0]
            merged = False

            if name in acc_table:
                for email in acc[1:]:
                    for email_set in acc_table[name]:
                        if email in email_set:
                            email_set.update(acc[1:])
                            merged = True
                            break

                    if merged:
                        break

                if not merged:  # no duplicate email exist
                    acc_table[name].append(set(acc[1:]))

            else:
                acc_table[name] = [set(acc[1:])]

        ans = []
        for name, acc_set_list in acc_table.items():
            for acc_set in acc_set_list:
                ans.append([name] + list(sorted(acc_set)))

        return ans
