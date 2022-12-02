#!/usr/bin/env python3
# @Date       : 2022/4/10 
# @Filename   : 6038.py
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
	def minimizeResult(self, expression: str) -> str:
		s1 = expression.split('+')
		left = s1[0]
		right = s1[1]

		total = int(left) + int(right)
		min_val = total
		for kh1 in range(0,len(left)):
			for kh2 in range(1,len(right)+1):
				if kh1 == 0 and kh2 == len(right):
					n1 = 1
					n2 = int(left)
					n3 = int(right)
					n4 = 1
				elif kh1 == 0: 
					n1 = 1
					n2 = int(left)
					n3 = int(right[0:kh2])
					n4 = int(right[kh2:])
				elif kh2 == len(right):
					n1 = int(left[0:kh1])
					n2 = int(left[kh1:])
					n3 = int(right)
					n4 = 1			
				else:
					n1 = int(left[0:kh1])
					n2 = int(left[kh1:])
					n3 = int(right[0:kh2])
					n4 = int(right[kh2:])

				val = n1 * (n2 +n3) * n4
				if val <= min_val:
					res_l = kh1
					res_r = kh2
					min_val = val
					

		ls1 = list(left)
		ls1.insert(res_l, '(') 
		left = ''.join(ls1)

		ls2 = list(right)
		ls2.insert(res_r, ')') 
		right = ''.join(ls2)

		return left + '+' + right
# -------------------------
		
a = Solution()
b = "247+38"
print(a.minimizeResult(b))