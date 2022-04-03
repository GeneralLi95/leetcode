#!/usr/bin/env python3
# @Date       : 2022/2/14 
# @Filename   : 540.py 有序数组中的单一元素
# @Tag        : 二分查找
# @Autor      : LI YAO
# @Difficulty : Medium

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
	def singleNonDuplicate(self, nums: List[int]) -> int:		
		n = len(nums)
		left = 0
		right = n - 1
		if n == 1:
			return nums
		while right - left > 1:
			mid = (right + left) // 2
			if nums[mid] == nums[mid^1]:  
				# 此处直接分类讨论了，如果 mid 是奇数的话相当于 nums[mid] = nums[mid - 1]
				# 如果mid 是偶数的话相当于 nums[mid] = nums[mid + 1]
				left = mid + 1    
				# 所以条件相当于奇数且与前一个数字相等 需要移动坐标
				# 或者偶数且与后一个数字相等，
			else:
				right = mid
				
			# 最终结束条件是 left = right 
		return nums[left]
# -------------------------
		
a = Solution()
b = [3,3,7,7,10,11,11]
b2 = [1,1,2,3,3,4,4,8,8]
print(a.singleNonDuplicate(b2))