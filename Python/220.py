#!/usr/bin/env python3
# @Date       : 2022/1/19 
# @Filename   : 220.py 存在重复元素3
# @Tag        : 桶排序，滑动窗口
# @Autor      : LI YAO
# @Difficulty : Medium

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
	def containsNearbyAlmostDuplicate(self, nums: List[int], k: int, t: int) -> bool:
		s = set()
		for i, num in enumerate(nums):
			print(s)
			if i > k:
				s.remove(nums[i - k - 1])
			if len(s) >=2 and max(s) - min(s) <= t:
				return True
			s.add(num)
		return False
		
# -------------------------
		
a = Solution()
b = [1,5,9,1,5,9]
b2 = [1,2,3,1]
c = 3
d = 0

print(Solution.containsNearbyAlmostDuplicate(a, b2, c, d))