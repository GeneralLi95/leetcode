#!/usr/bin/env python3

class ListNode:
	def __init__(self, val=0, next=None):
		self.val = val
		self.next = next
		
		
class Solution:
	def removeElements(self, head: ListNode, val: int) -> ListNode:
		
		p1 = p2 = ListNode()
		while head:
			if head.val == val:
				head = head.next
			else:
				p2.next = head
				p2 = p2.next
				head = head.next
		return p1.next
		
a = Solution()

l1 =ListNode(1)
l1.next = ListNode(2)
l1.next.next = ListNode(4)



result = Solution().removeElements(head = l1,val = 2)

while result:
	print(result.val)
	result = result.next