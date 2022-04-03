#!/usr/bin/env python3
# @Date       : 2022/2/9 
# @Filename   : 2006.py
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
	def countKDifference(self, nums: List[int], k: int) -> int:		
		nums.sort()
		num_hash = Counter(nums)
		res = 0
		for num, cnt in num_hash.items():
			if num + k in num_hash:
				res += cnt * num_hash[num+k]
				
		
		return res
		
		
# -------------------------
		
a = Solution()
b = [3,2,1,5,4]
c = 2

a.countKDifference(b, c)