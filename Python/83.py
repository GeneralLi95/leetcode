#!/usr/bin/env python3

#!/usr/bin/env python3

class ListNode:
	def __init__(self, val=0, next=None):
		self.val = val
		self.next = next
		
		
class Solution:
	def deleteDuplicates(self, head: ListNode) -> ListNode:
		
		p1 = p2 = head
		if p2 == None:
			return head
		while True:
#			print('node',node.val, 'p1', p1.val)
			if p2 == None or p2.val != p1.val:
				p1.next = p2
				p1 = p1.next
			if p2 == None:
				break
			p2 = p2.next
			
		return head
	
a = Solution()

l1 =ListNode(1)
l1.next = ListNode(1)
l1.next.next = ListNode(2)
l1.next.next.next = ListNode(2)



result = Solution().deleteDuplicates(head = l1)

while result:
	print(result.val)
	result = result.next