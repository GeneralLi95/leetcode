#!/usr/bin/env python3
# 链表随机节点
# 2022-01-16
# Medium
# 水塘抽样


from heapq import *
from typing import List,  Optional
from collections import defaultdict, deque
from itertools import product,combinations,permutations
from random import choice, randrange

class ListNode: 
	def __init__(self, val=0, next=None):
		self.val = val
		self.next = next

# -------------------------
# 方法1 记录所有的链表元素，化链表为数组，时间复杂度 O(n), 空间复杂度O(n)
#class Solution:
#	def __init__(self, head: Optional[ListNode]):
#		self.arr = []
#		while head:
#			self.arr.append(head.val)
#			head = head.next
#		
#		
#	def getRandom(self) -> int:
#		return choice(self.arr)
	
# -------------------------
# 方法2 蓄水池抽样，时间复杂度 O(n),空间复杂度O(1)，不需要存储链表元素值
class Solution:
	def __init__(self, head: Optional[ListNode]):
		self.head = head
			
			
	def getRandom(self) -> int:
		node, i, ans = self.head, 1, 0
		while node:
			if randrange(i) == 0:
				ans = node.val
			i += 1
			node = node.next
		return ans
# -------------------------
l1 =ListNode(1)
l1.next = ListNode(2)
l1.next.next = ListNode(3)
l1.next.next.next = ListNode(4)

obj = Solution(head=l1)
a = [0,0,0,0]
for i in range(100):
	temp = obj.getRandom()
	if temp == 1:
		a[0] += 1
	if temp == 2:
		a[1] += 1
	if temp == 3:
		a[2] += 1
	if temp == 4:
		a[3] += 1
print(a)