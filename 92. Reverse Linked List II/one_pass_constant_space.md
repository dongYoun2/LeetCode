## One-pass Constant Space Implementation

[Problem](https://leetcode.com/problems/reverse-linked-list-ii/)

The code below is from one of the comments in the LeetCode Editorial's discussion. I first attempted the problem very similar to this logic, but debugging took too long; so I restarted from scratch after deciding to use extra space for storing nodes' addresses in the array.

- TC: $O(n)$, wheren $n$is the number of nodes in the linked list
- SC: $O(1)$

```c
ListNode *reverseBetween(ListNode *head, int left, int right) {
   int curIdx = 1;
   ListNode *beforeLeft = nullptr;
   ListNode *prev = nullptr, *cur = head, *nxt = nullptr;
   ListNode *leftPtr = nullptr;
   while (cur) {
       nxt = cur->next;
       if (curIdx == left - 1) {
           beforeLeft = cur;
       } else if (curIdx == left) {
           leftPtr = cur;
       } else if (curIdx > left && curIdx < right) {
           cur->next = prev;
       } else if (curIdx == right) {
           leftPtr->next = cur->next;
           cur->next = prev;
           if (beforeLeft) {
               beforeLeft->next = cur;
               return head;
           } else {
               return cur;
           }
       }
       curIdx++;
       prev = cur;
       cur = nxt;
   }
   return head;
}
```