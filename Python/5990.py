#!/usr/bin/env python3
# @Date       : 2022/1/23 
# @Filename   : 5990.py
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
	def findLonely(self, nums: List[int]) -> List[int]:		
		if len(nums) == 1:
			return nums
		nums.sort()
		result = []
		for i in range(0, len(nums)):
			if i == 0:
				if nums[i+1] not in [nums[i]-1,nums[i], nums[i]+1]:
					result.append(nums[i])
				continue
			if i == len(nums)-1:
				if nums[i-1] not in  [nums[i]-1,nums[i], nums[i]+1]:
					result.append(nums[i])
				break
			if nums[i+1] not in [nums[i]-1,nums[i], nums[i]+1] and nums[i-1] not in  [nums[i]-1,nums[i], nums[i]+1]:
				result.append(nums[i])
				
		return result
			
		
# -------------------------
		
a = Solution()
b = [10,6,5,8]
b2 = [1,3,5,3]
print(Solution.findLonely(a, b2))