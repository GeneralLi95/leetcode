#!/usr/bin/env python3
# @Date       : 2022/3/13 
# @Filename   : 6031.py
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
	def findKDistantIndices(self, nums: List[int], key: int, k: int) -> List[int]:		
		n = len(nums)
		result = []
		for i in range(n):
			for j in range(n):
				if abs(i-j) <= k and nums[j] == key:
					result.append(i)
					break
		return result
		
# -------------------------
		
a = Solution()
nums1 = [3,4,9,1,3,9,5]
nums2 = [2,2,2,2,2]
key1 = 9
k1 = 1

print(a.findKDistantIndices(nums2, 2, 2))