#!/usr/bin/env python3

from typing import List,  Optional
from collections import defaultdict, deque
from itertools import product,combinations,permutations

class ListNode: 
	def __init__(self, val=0, next=None):
		self.val = val
		self.next = next

# -------------------------
class Solution:
	def increasingTriplet(self, nums: List[int]) -> bool:
		small = mid = inf
		for num in nums:
			if num <= small:
				small = num
			elif num <= mid:
				mid = num
			else:
				return True
		return False
		
		
# -------------------------
		
a = Solution()
b = [2,1,5,0,4,6]
Solution.increasingTriplet(a, b)