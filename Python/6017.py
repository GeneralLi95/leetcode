#!/usr/bin/env python3
# @Date       : 2022/3/6 
# @Filename   : 6017.py
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
	def minimalKSum(self, nums: List[int], k: int) -> int:
		nums = list(set(nums))
		
		nums.sort()

		q = deque(nums)
		result = []
		i = 1
		left = 0
		right = q.popleft()
		rs = 0
		while k > 0:
			if k >= (right - left):
				rs = rs + (right - left - 1) * (left+1) + (right - left - 1 ) * (right - left - 2) // 2
				k -= (right - left - 1 )
				left = right
				if q:
					right = q.popleft()
				else:
	
					rs = rs + k * (left + 1) + k * (k -1) // 2

					break
			else:
				rs = rs + k * (left + 1) + k * (k -1) // 2
				k = 0

		return rs
		
		
# -------------------------
		
a = Solution()
nums1 = [1,4,25,10,25]
k1 = 2

nums2 = [5,6]
k2 = 6


nums3 = [96,44,99,25,61,84,88,18,19,33,60,86,52,19,32,47,35,50,94,17,29,98,22,21,72,100,40,84]
k3 = 35  
# 794
print(a.minimalKSum(nums3, k3))