# submission: https://leetcode.com/problems/sort-list/submissions/2031280248/
# runtime: 211 ms (beats 17.81%), memory: 40.58 MB (beats 88.53%)
# 35 min
# solved with recursive merge sort (divide and conquer)

# refer to the "05_29_2025.py" solution for a complexity analysis


# after solving with "06_12_2026.py" solution, and as mentioned there that the problem's intention is not using python's built-in sorting, i tried to solve the follow-up question. to solve this problme in a constant space, i realized i need to implement the merge sort, espeically in an iterative manner. however, i somehow tried to solve in a recursive manner. i properply code the `merge(...)` function, but stuck on the `merge_sort(...)`. so, wit the help of chatgpt for the basic implementation structure of array merge sort, i was able to implmeent `merge_sort(...)` as well, and solve the problem.

# note that it's still not a constant space solution since it's a recursive merge sort solution. for a follow-up question's solution, refer to the "follow_up.md" file.

# cf.) good chance to review the merge sort algorithm.

# cf.) the algorithm is similar to the "05_29_2025.py" solution, but the only difference is that i used slow and fast pointer technique for splitting the list into halves here, whereas in "05_29_2025.py" i utilized the number of nodes in the list.


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]: 
        def merge(a, b):
            aa, bb = a, b
            dummy = curr = ListNode(-1)

            while aa and bb:
                if aa.val < bb.val:
                    curr.next = aa
                    aa = aa.next
                else:
                    curr.next = bb
                    bb = bb.next
                
                curr = curr.next

            rest = aa or bb
            if rest:
                curr.next = rest

            return dummy.next

        
        def merge_sort(node):
            if node is None or node.next is None:
                return node

            dummy = ListNode(-1)
            dummy.next = node
            slow = fast = dummy
            while fast and fast.next:
                fast = fast.next.next
                slow = slow.next

            right_half = slow.next
            
            slow.next = None
            left_half = dummy.next

            merged_left = merge_sort(left_half)
            merged_right = merge_sort(right_half)

            merged = merge(merged_left, merged_right)

            return merged


        return merge_sort(head)
