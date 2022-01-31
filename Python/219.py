#!/usr/bin/env python3
# @Date       : 2022/1/19 
# @Filename   : 219.py 存在重复元素2
# @Tag        : 滑动窗口
# @Autor      : LI YAO
# @Difficulty :

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
# 方法1 哈希表 
class Solution:
	def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
		count = defaultdict(list)
		for id, num in enumerate(nums):
			if count[num]:
				if id - count[num][-1] <= k:
					return True
				else:
					count[num].append(id)
			else:
				count[num].append(id)
		return False
# -------------------------
# 方法2 滑动窗口 
class Solution:
	def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
		window = deque()
		for i, num in enumerate(nums):
			if i > k:
				window.popleft()
			if num in window:
				return True
			window.append(num)
		return False
	
# --------------------------	
# 用集合实现滑动窗口
class Solution:
	def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
		s = set()
		for i, num in enumerate(nums):
			if i > k:
				s.remove(nums[i - k - 1])
			if num in s:
				return True
			s.add(num)
		return False
# -------------------------
		
a = Solution()
b = [1,2,3,1,2,3]
c = 2
print(Solution.containsNearbyDuplicate(a, b,c))