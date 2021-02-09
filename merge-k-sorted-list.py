# https://leetcode.com/problems/merge-k-sorted-lists/


# You are given an array of k linked-lists lists, each linked-list is sorted in ascending order.

# Merge all the linked-lists into one sorted linked-list and return it.

 

# Example 1:

# Input: lists = [[1,4,5],[1,3,4],[2,6]]
# Output: [1,1,2,3,4,4,5,6]
# Explanation: The linked-lists are:
# [
#   1->4->5,
#   1->3->4,
#   2->6
# ]
# merging them into one sorted list:
# 1->1->2->3->4->4->5->6

# Example 2:

# Input: lists = []
# Output: []
# Example 3:

# Input: lists = [[]]
# Output: []



# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        def merge(i,d):
            l3 = head= ListNode()
            l1, l2 = lists[i], lists[d]
            while l1 and l2:
                mini = min(l1.val, l2.val)
                if mini == l1.val:
                    head.next = l1
                    head = head.next
                    l1 = l1.next
                if mini == l2.val:
                    head.next = l2
                    head = head.next
                    l2 = l2.next
            if l1:
                head.next = l1
            if l2:
                head.next = l2
            return l3.next
       
        d = 1
        while d < len(lists):
            i = 0
            while i+d< len(lists):
                lists[i] = merge(i, i+d)
                i += d*2
            d *= 2
        return (lists[0] if lists[0] else None) if lists else None
            
        