#!/usr/bin/env python3
# @Date       : 2022/3/13 
# @Filename   : 5227.py
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
	def maximumTop(self, nums: List[int], k: int) -> int:		
		stack = deque(nums)
		if k == 0 :
			return nums[0]
		result = 0
		
		if len(nums) == 1 and k % 2 == 1:
			return -1
		
		if k > len(nums):
			return max(nums) 

		for i in range(k):
#			if i == 0:
#				temp = stack.popleft()
#				result = max(result, temp)
#				if not stack:
#					return -1
			if i == (k-1):
				temp = stack.popleft()
				if len(stack) >= 1:
					top_temp = stack[0]
				else:
					top_temp = 0
				result = max(result, top_temp)
			else:
				temp = stack.popleft()
				result = max(result,temp)
		return result
				
		
# -------------------------
		
a = Solution()

b = [5,2,2,4,0,6]
c = 4

b2 = [2]
c2 = 2

b3 = [1,2]
c3 = 1


b4 = [ 1,2,3]
c4 = 4

b5 = [4,6,1,0,6,2,4]
c5 = 0


b6 = [3,2,1]
c6 = 1
print(a.maximumTop(b5, c5))