#!/usr/bin/env python3

# 判断链表是否有环
class ListNode:
	def __init__(self, x):		
		self.val = x
		self.next = None
		
		

	
class Solution:
	def hasCycle(self, head: ListNode) -> bool:
		return None

first = LinkList()
first = LinkList.initlist_tail(first, [1, 2, 3])
#print(first.length)

l1_0 = ListNode(0)
l1_2 = ListNode(2)
l2_0 = ListNode(1)
l2_2 = ListNode(4)

l1_0.next = l1_2
l2_0.next = l2_2


	