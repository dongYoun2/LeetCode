# submission: https://leetcode.com/problems/insert-delete-getrandom-o1/submissions/2082555465/
# runtime: 132 ms (beats 29.99%), memory: 56.80 MB (beats 89.35%).
# 12 min
# solved with hash table and array


# when i failed to solve on 09/01/2025, i was flabbergasted by removing a certain element in the array in O(1) time by swapping it with the last element then popping the last element! so i was able to come up with that idea quite fast.


import random


class RandomizedSet:

    def __init__(self):
        self.arr = []
        self.v2idx = {}
        

    def insert(self, val: int) -> bool:
        if val in self.v2idx:
            return False

        self.arr.append(val)
        self.v2idx[val] = len(self.arr) - 1

        return True
        

    def remove(self, val: int) -> bool:
        if val not in self.v2idx:
            return False
        
        pos = self.v2idx[val]
        last = len(self.arr)-1
        swap_val = self.arr[last]

        self.arr[pos], self.arr[last] = self.arr[last], self.arr[pos]
        self.v2idx[swap_val] = pos
        del self.v2idx[val]
        self.arr.pop()

        return True


    def getRandom(self) -> int:
        pos = random.randrange(len(self.arr))
        
        return self.arr[pos] 


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
