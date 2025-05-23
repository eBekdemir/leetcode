# URL: https://leetcode.com/problems/merge-nodes-in-between-zeros/                        
# TITLE: Merge Nodes in Between Zeros                            
# DIFFICULTY: Medium                                
# ------------------------------------------------------
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeNodes(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        result = ListNode()
        mem = result
        sm = 0
        while head.next:
            head = head.next
            if head.val != 0:
                sm += head.val
            else:
                mem.next = ListNode(sm)
                mem = mem.next
                sm = 0
        return result.next
                