#!/usr/bin/env python3

from typing import List, Optional
class ListNode:
	def __init__(self, val=0, next=None):
		self.val = val
		self.next = next
		
		
class Solution:
	def deleteMiddle(self, head: [ListNode]) -> Optional[ListNode]:
		
		p1 = head
		p2 = p3 = head
		length = 0
		
		while p1:
			length += 1
			p1 = p1.next
		if length == 1:
			return None
		middle = length // 2
		temp = 0
		while p3:
			if (temp+1) == middle:
				p3.next = p3.next.next 
			else:
				p3 = p3.next 
			temp+=1
			
		return p2
	
a = Solution()

l1 =ListNode(1)
#l1.next = ListNode(2)
#l1.next.next = ListNode(3)
#l1.next.next.next = ListNode(4)


result = Solution.deleteMiddle(a, l1)
while result:
	print(result.val)
	result = result.next