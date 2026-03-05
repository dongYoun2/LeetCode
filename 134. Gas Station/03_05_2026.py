# submission: https://leetcode.com/problems/gas-station/submissions/1939168078/
# runtime: 30 ms (beats 42.55%), memory: 26.01 MB (beats 65.68%)
# 35 min

# time and space complexity analysis is the same as the README.md. refer to that for details.


# having solved this problem several times, i knew i had to use a greedy approach. however, i got stuck while coding up the solution due to several edge cases. also, i still feel greedy approach is quite tricky.


class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        n = len(gas)
        ans = 0
        total = curr_tank = gas[0] - cost[0]

        for i in range(1, n):
            if curr_tank < 0:
                curr_tank = 0
                ans = i
            
            remain = gas[i] - cost[i]
            total += remain
            curr_tank += remain

        return -1 if total < 0 else ans


# notes while solving:
# idx:            0   1   2   3   4
# gas:            1   2   3   4   5
# cost:           3   4   5   1   2
# gas - cost:    -2  -2  -2   3   3


# ans_idx = 3
# curr_idx = 2
# curr_gas = 0


# gas - cost:  1  5  -8  3  1