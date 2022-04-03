#!/usr/bin/env python3
# @Date       : 2022/3/27 
# @Filename   : Untitled.txt
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
	def minDeletion(self, nums: List[int]) -> int:
		cnt = 0
		i = 0

		for i in range(len(nums)-1):
			if i % 2 == 0 and nums[i] == nums[i+1] and cnt % 2 == 0:
				cnt += 1



			if i % 2 == 1 and cnt % 2 == 1 and nums[i] == nums[i+1]:
				cnt += 1


		if (len(nums) - cnt) % 2 == 1:
			cnt += 1

		return cnt
		
		
# -------------------------
		
a = Solution()
b = [1,1,2,2,3,3]
b2 = [1,1,2,3,5]
b3 = [1]
b4 = [6,6,6,0,1,7,1,9,4,9,3,3,4,5,0,3,8,7,1,8,4,5] # 4 
print(a.minDeletion(b4))