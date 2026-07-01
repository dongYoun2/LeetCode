# submission: https://leetcode.com/problems/design-hit-counter/submissions/2051224928/
# runtime: 0 ms (beats 100.00%), memory: 19.33 MB (beats 76.47%)
# 39 min
# solved using prefix sum + binary search
# this solves the follow-up question: "What if the number of hits per second could be huge? Does your design scale?"

# symbols:
# - n: number of hits
# - u: unique timestamps (u <= n)

# TC:
# - hit(): O(1)
# - getHits(): O(u)
# SC (of the entire object): O(u)


# i simulated the process of this problem. i also looked at the follow-up question in the beginning. to make the solution scale when there are multiple hits at the same timestamp, i approached somehow storing the frequency (or count) of hits at one timestamp. then i realized if i store the cumulative sum of hits at each timestamp, which i can achieve by using a prefix sum, the answer for the `getHits()` method would be simply (cumulative count at the largest timestamp less than or equal to the given `timestamp`) - (cumulative count at the largest timestamp less than or equal to the given `timestamp` - 300). therefore, if we save the (timestamp, cumulative count) pairs in a list, we can use a binary search to find the corresponding cumulative hit counts for two timestamps.

# cf.) we actually don't need to check if the `self.hits` is empty since we initialized it with a dummy hit in a constructor. this submission can be found here: https://leetcode.com/problems/design-hit-counter/submissions/2051527574/

# cf.) though i used a binary search to solve this problem, there are more efficient approaches as well. refer to the README.md for details.


import bisect


class HitCounter:

    def __init__(self):
        self.hits = [[-400, 0]] # dummy hit
        

    def hit(self, timestamp: int) -> None:
        if not self.hits:
            self.hits.append([timestamp, 1])
            return
         
        if self.hits[-1][0] == timestamp:
            self.hits[-1][1] += 1
        else:
            cum_hit_cnt = self.hits[-1][1]
            self.hits.append([timestamp, cum_hit_cnt + 1])
        

    def getHits(self, timestamp: int) -> int:
        t_from = timestamp - 300

        from_idx = bisect.bisect(self.hits, t_from, key=lambda e: e[0])
        to_idx = bisect.bisect(self.hits, timestamp, key=lambda e: e[0])

        return self.hits[to_idx-1][1] - self.hits[from_idx-1][1]


# Your HitCounter object will be instantiated and called as such:
# obj = HitCounter()
# obj.hit(timestamp)
# param_2 = obj.getHits(timestamp)
