#!/usr/bin/env python3
# @Date       : 2022/3/27 
# @Filename   : 5253.py
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
	def kthPalindrome(self, queries: List[int], intLength: int) -> List[int]:
		total = 1
		for i in range(intLength//2 + intLength % 2):
			if i == 0:
				total *= 9
			else:
				total *= 10
		result = []
		for q in queries:
			if q > total:
				result.append(-1)
			else:
				huiwen = ''
				n = intLength//2 + intLength % 2
				for i in range(n):
					if i == 0:
						huiwen += str((q-1)//10+1)
					else:
						huiwen += str((q-1) % (10 ** (n-i)))
				print(q, huiwen)
				if intLength % 2 == 0:		
#					print(q, huiwen + huiwen[::-1])
					result.append(int(huiwen + huiwen[::-1]))
				else:
#					print(q, huiwen[:-1] + huiwen[::-1])
					result.append(int(huiwen[:-1] + huiwen[::-1]))
		return result
		
		
# -------------------------
		
a = Solution()
q1 = [1,2,3,4,5,6,7,8,9,10,11,54,90,899]
il1 = 3
q = [2,4,6]
il = 4

q3 = [2,201429812,8,520498110,492711727,339882032,462074369,9,7,6] # [2,-1,8,-1,-1,-1,-1,9,7,6]
il3 = 1
print(a.kthPalindrome(q1, 5))