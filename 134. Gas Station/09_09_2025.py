# submission: https://leetcode.com/problems/gas-station/submissions/1765008222/
# runtime: 27 min, memory: 23.8 MB

# 43 min
# TC: O(n), where n is the length of gas (or cost)
# SC: O(n) - tank array
# cf.) SC can be reduced to O(1) by computing tank on the fly instead of storing it in an array


# it took me a while to solve this problem. the code below is a greedy solution. personally, i feel hard to find whether the problem is a greedy problem as well as to come up with a greedy approach if it is.

# `cumsum` is the current amount of gas (`curr_gas` in README.md) from where we start. starting index `start` is updated based on the `cumsum` and the current tank value `tank[i]`. actullay, this code can be improved only by checking the `cumsum` value to update `start`.

# moreover, the code can be optimized to use the one-pass algorithm. currently, the code below uses two-pass (one for early return for impossible case, the other for finding the starting index if possible). instead, we can check the total amount of gas on the fly while finding the starting index. (but this is trivial, and sometimes, early return is better.)

# cf.) the code in the README.md reflects all the improvements mentioned above. refer to the README.md for more details.


class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        n = len(gas)
        tank = [gas[i] - cost[i] for i in range(n)]

        if sum(tank) < 0: return -1

        start = 0
        cumsum = tank[0]
        for i in range(1, n):
            if cumsum < 0 and tank[i] >= 0:
                start = i
                cumsum = tank[i]
            else:
                cumsum += tank[i]

        return start


# notes while solving:
# gas:      1  2  3  4 5
# cost:     3  4  5  1 2
# tank:    -2 -2 -2  3 3

# gas:      2  3 4
# cost:     3  4 3
# tank:     -1 -1 1

# tank (diff. case): -1 -1 -1 3 -6 8