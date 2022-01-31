#!/usr/bin/env python3
# @Date       : 2022/1/16 ___TIME___
# @Filename   : 398.py
# @Tag        : 水塘抽样
# @Autor      : LI YAO
# @Difficulty : Medium

from heapq import *
from typing import List,  Optional
from collections import defaultdict, deque
from itertools import product,combinations,permutations
from random import choice, randrange

class ListNode: 
	def __init__(self, val=0, next=None):
		self.val = val
		self.next = next

# -------------------------
class Solution:
	
	def __init__(self, nums: List[int]):
		self.nums = nums
		
	def pick(self, target: int) -> int:
		count = 1
		for id, x in enumerate(self.nums):
			if x == target:
				if randrange(count) == 0:
					result = id
				count += 1
		return result
		
		
# -------------------------
		

a = [1,2,3,3,3]

obj = Solution(a)
print(obj.pick(3))