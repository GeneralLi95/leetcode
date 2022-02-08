#!/usr/bin/env python3
# @Date       : 2022/2/6 
# @Filename   : 600.py
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
	def sortEvenOdd(self, nums: List[int]) -> List[int]:
		if len(nums) <= 2:
			return nums
		n1 = []
		n2 = []
		for i, num in enumerate(nums):
			if i % 2 == 0:
				n1.append(num)
			else:
				n2.append(num)
		
		n1.sort(reverse = False)
		n2.sort(reverse = True)
		result = [0 for _ in range(len(nums))]
		
		
			
		print(n1,n2)
			
		for i in range(len(nums)):
			if i % 2 == 0:
				result[i] = n1[i//2]
			else:
				result[i] = n2[i//2]

				
		return result
		
# -------------------------
		
a = Solution()

b = [4,1,2,3]
print(a.sortEvenOdd(b))