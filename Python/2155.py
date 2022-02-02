#!/usr/bin/env python3
# @Date       : 2022/2/2 
# @Filename   : 2155.py
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
	def maxScoreIndices(self, nums: List[int]) -> List[int]:
		n = len(nums)
		score = nums.count(1)
		max_score = nums.count(1)
		id = [0]
		for i, num in enumerate(nums):
			if num == 0:
				score = score + 1
			if num == 1:
				score = score - 1
			if score > max_score:
				max_score = score
				id = [i+1]
			elif score == max_score:
				id.append(i+1)
		return id		
		
		
# -------------------------
		
a = Solution()
b = [0,0,1,0]
print(a.maxScoreIndices(b))