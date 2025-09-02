# submission: https://leetcode.com/problems/insert-delete-getrandom-o1/submissions/1756403824/

# 55 min


# From LeetCode Top Interview 150 - Array / String

# the code below is a wrong implementation (it's almost close). the only thing to change is adding a `latest_val` and `val` equality checks in the `remove(...)` method. without them, the same value will be reinserted after removing it. the correct implementation can be found at https://leetcode.com/problems/insert-delete-getrandom-o1/submissions/1756412294/.

# moreover, instead of keeping both index to val and val to index mappings, we can simply keep a list of values and a val to index mapping, which is the same approach explained in the Editorial section. in this way, we don't need to check the equality of the latest value and the value being removed.

# TAKEAWAY: if the order doesn't have to be preserved, removing element in the list can be done in O(1) time by swapping it with the last element and popping the last element!


import random

class RandomizedSet:

    def __init__(self):
        self.size = 0
        self.idx_to_val = {}
        self.val_to_idx = {}


    def insert(self, val: int) -> bool:
        if val in self.val_to_idx:
            return False

        new_idx = self.size
        self.idx_to_val[new_idx] = val
        self.val_to_idx[val] = new_idx

        self.size += 1

        return True


    def remove(self, val: int) -> bool:
        if val not in self.val_to_idx:
            return False

        orig_idx = self.val_to_idx[val]
        latest_val = self.idx_to_val[self.size-1]

        # remove from val_to_idx
        del self.val_to_idx[val]
        self.val_to_idx[latest_val] = orig_idx

        # remove from idx_to_val
        self.idx_to_val[orig_idx] = latest_val
        del self.idx_to_val[self.size-1]

        self.size -= 1

        return True


    def getRandom(self) -> int:
        rand_n = random.randint(0, self.size-1)
        return self.idx_to_val[rand_n]


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
