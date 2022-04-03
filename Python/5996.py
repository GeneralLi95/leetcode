#!/usr/bin/env python3
# @Date       : 2022/2/19 
# @Filename   : 5996.py
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
	def countPairs(self, nums: List[int], k: int) -> int:	
		dic = defaultdict(list)
		res = 0
		for i, num in enumerate(nums):
			dic[num].append(i)
			
		for item in dic.items():
			if len(item[1]) == 1:
				continue
			
			for i in range(len(item[1]) - 1):
				for j in range(i+1,len(item[1])):
					if item[1][i] * item[1][j] % k == 0:
						res += 1
						
						
		return res
				

		
# -------------------------
		
a = Solution()

b = [3,1,2,2,2,1,3]
c = 2
print(a.countPairs(b, c))