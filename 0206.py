# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseList(self, head):
        prev, curr = None, head
        
        while curr:
            nextt = curr.next 
            curr.next = prev
            prev = curr
            curr = nextt

        return prev


# ------------------------------------------------------
class Solution(object):
    def reverseList(self, head):
        theList = []
        curr = head
        while curr:
            theList.append(curr.val)
            curr = curr.next

        res = ListNode()
        curr = res
        for v in theList[::-1]:
            curr.next = ListNode(v)
            curr = curr.next

        return res.next
 
