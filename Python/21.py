#!/usr/bin/env python3


class ListNode:
	def __init__(self, val=0, next=None):
		self.val = val
		self.next = next


class Solution:
	def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
		
		head = ListNode()
		p = head
		while l1 and l2:
			if l1.val <= l2.val:
				p.next=l1
				l1 = l1.next
				p = p.next
				p.next = None
			else:
				p.next = l2
				l2 = l2.next
				p = p.next 
				p.next = None
		if l1:
			p.next = l1
		if l2:
			p.next = l2
		return head.next
	
a = Solution()

l1 =ListNode(1)
l1.next = ListNode(2)
l1.next.next = ListNode(4)

l2 = ListNode(1)
l2.next = ListNode(3)
l2.next.next = ListNode(4)

result = Solution().mergeTwoLists(l1 = l1, l2 = l2)

while result:
	print(result.val)
	result = result.next