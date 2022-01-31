#!/usr/bin/env python3
# @Date       : 2022/1/19 
# @Filename   : 217.py 存在重复元素
# @Tag        : 哈希表，排序
# @Autor      : LI YAO
# @Difficulty : Easy

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
#class Solution:
#	def containsDuplicate(self, nums: List[int]) -> bool:
#		count = defaultdict(list)
#		for id, num in enumerate(nums):
#			count[num].append(id)
#		for i in count:
#			if len(count[i]) > 1:
#				return True
#		return False
# ------------------------
# 方法2 排序
#class Solution:
#	def containsDuplicate(self, nums: List[int]) -> bool:
#		nums.sort()
#		for i in range(1,len(nums)):
#			if nums[i] == nums[i-1]:
#				return True
#		return False
# -------------------------
# 方法3 集合
class Solution:
	def containsDuplicate(self, nums: List[int]) -> bool:
		if len(nums) != len(set(nums)):
			return True
		return False
# -------------------------
		
a = Solution()
b = [1,1,1,3,3,4,3,2,4,2]
Solution.containsDuplicate(a, b)