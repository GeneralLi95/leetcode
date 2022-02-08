#!/usr/bin/env python3
# @Date       : 2022/2/5 
# @Filename   : untitled file.py
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
	def pivotArray(self, nums: List[int], pivot: int) -> List[int]:		
		n = len(nums)
		if n == 1:
			return nums
		left = []
		mid = []
		right = []
		
		for num in nums:
			if num < pivot:
				left.append(num)
				
			if num == pivot:
				mid.append(num)
				
			if num > pivot:
				right.append(num)
				
				
		return left + mid + right
# -------------------------
		
a = Solution()

b = [9,12,5,10,14,3,10]

c = 10

print(a.pivotArray(b, c))