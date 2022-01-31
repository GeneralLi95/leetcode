#!/usr/bin/env python3
# @Date       : 2022/1/23 
# @Filename   : 5991.py
# @Tag        :
# @Autor      : LI YAO
# @Difficulty :

from heapq import *
from typing import List,  Optional
from collections import defaultdict, deque
from itertools import product,combinations,permutations,accumulate
from random import choice, randrange,randint

class ListNode: 
	def __init__(self, val=0, next=None):
		self.val = val
		self.next = next

# -------------------------
class Solution:
	def rearrangeArray(self, nums: List[int]) -> List[int]:
		stack1 = []
		stack2 = []
		result = [0 for _ in range(len(nums))]
		for i in nums:
			if i > 0:
				stack1.append(i)
			else:
				stack2.append(i)
#		print(stack1,stack2)
		for i in range(len(nums)//2):
			result[2*i] = stack1[i]
			result[2*i+1] = stack2[i]
			
		return result
		
# -------------------------
		
a = Solution()
b = [3,1,-2,-5,2,-4]
Solution.rearrangeArray(a, b)