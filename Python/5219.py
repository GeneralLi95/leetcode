#!/usr/bin/env python3
# @Date       : 2022/4/3 
# @Filename   : 5219.py
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
	def maximumCandies(self, candies: List[int], k: int) -> int:		
		if sum(candies) < k:
			return 0
		def count(x, candies):
			sum = 0
			for i in candies:
				sum += i//x
			return sum
		
		left = max(candies) // k
		right = 10000
		while left + 1 < right:
			mid = (left + right) // 2
			if count(mid, candies) >= k:
				left = mid
			else:
				right = mid
		return left
			
		
		
# -------------------------
		
a = Solution()
ca = [5,20,6]
k1 = 3

print(a.maximumCandies(ca, k1))