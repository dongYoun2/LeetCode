# submission: https://leetcode.com/problems/merge-k-sorted-lists/submissions/1900286484/
# runtime: 11 ms (beats 60.98%), memory: 23.07 MB (beats 17.67%)
# 30 min

# - k: number of linked lists
# - N: total number of nodes across all linked lists

# - TC: O(N log k), one pop/push per node (N nodes), and heap size at most k
# - SC: O(k), heap holds at most k nodes

# cf.) for a heap size T, time complexity of heapify (from scratch), push, and pop operations are O(T), O(log T), and O(log T), respectively.


# From LeetCode Top Interview 150 - Divide & Conquer


# though i selected from the divide & conquery category, i thought the category was linked list haha. by looking at the constraints, i thought this problem should be solved in O(N log N) or O(N) time (N: total number of nodes). noticing all nodes should be visited and the problem is a linked list problem, i though of creating python list to keep track of current pointer (node) for each linked list. however, i realized i don't need to do this since i can 1) use heap to find the smallest node across all current nodes, where each current corresponds to one linked list, and 2) find the next node of the current selected (smallest) node, which i can push it to the heap repeatedly.

# one trick i used to insert the equal priority nodes is to add a 3-element tuple, where the second element is the entry count. this can be seen as a timestamp which serves as a tie-breaker. other two approaches to address this is 1) defining custom `HeapNode` class with `__lt__`magic method or 2) defining custom `PrioritizedItem` dataclass with `field(compare=False)`.


import heapq

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        entry_cnt = 0
        heap_nodes = []
        for head in lists:
            if head is not None:
                entry_cnt += 1
                heap_nodes.append((head.val, entry_cnt, head))


        heapq.heapify(heap_nodes)

        # dummy node
        ans_dummy = ListNode(-1) 
        ans_curr = ans_dummy

        while heap_nodes:
            _, _, ptr = heapq.heappop(heap_nodes)
            ans_curr.next = ptr
            ans_curr = ans_curr.next

            assert ans_curr is not None

            if ptr.next is not None:
                entry_cnt += 1
                heapq.heappush(heap_nodes, (ptr.next.val, entry_cnt, ptr.next))
        
        return ans_dummy.next
