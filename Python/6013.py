#!/usr/bin/env python3
# @Date       : 2022/2/20 
# @Filename   : 6013.py
# @Tag        :
# @Autor      : LI YAO
# @Difficulty :

from heapq import *
from typing import List,  Optional
from collections import defaultdict, deque, Counter
from itertools import product,combinations,permutations,accumulate
from random import choice, randrange,randint

class ListNode: 
	def __init__(self, val=0, next=None):
		self.val = val
		self.next = next

# -------------------------
class Solution:
	def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:		
		dummy_head = ListNode(next=head) # 添加虚拟节点
		
		cur = dummy_head # cur 指针
		
		l = []
		temp = 0
		while(cur):
			if cur.val == 0 and temp !=0:
				l.append(temp)
				temp = 0
			else:
				temp += cur.val
			cur = cur.next
		print(l)
		res = ListNode(next=head)
		cur2 = res
		for i in l:
			cur2 = cur2.next
			cur2.next = ListNode(i)
			
		return res.next.next
		
# -------------------------
		
a = Solution()
h = ListNode()
c = h
b = [1,0,3,0,2,2,0]
for i in b:
	c.next = ListNode(i)
	c = c.next

res = a.mergeNodes(h)

while res:
	print(res.val)
	res = res.next