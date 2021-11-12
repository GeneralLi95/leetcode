#!/usr/bin/env python3

class ListNode:
	def __init__(self, val=0, next=None):
		self.val = val
		self.next = next
		
		
class Solution:
	def reverseList(self, head: ListNode) -> ListNode:
		result = []
		
		while head:
			node = head
			head = head.next
			node.next = None

			result.append(node)
			
		p1 = p2 = ListNode
		for i in range(len(result)):
			p2.next = result[-i-1]
			p2 = p2.next
		return p1.next
	
a = Solution()

l1 =ListNode(1)
l1.next = ListNode(2)
l1.next.next = ListNode(4)



result = Solution().reverseList(head = None)

while result:
	print(result.val)
	result = result.next