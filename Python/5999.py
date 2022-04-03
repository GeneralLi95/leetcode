#!/usr/bin/env python3
# @Date       : 2022/2/19 
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
	def goodTriplets(self, nums1: List[int], nums2: List[int]) -> int:
		dic1 = {}
		dic2 = {}
		
		for i, num in enumerate(nums1):
			dic1[num] = i
			
		for i, num in enumerate(nums2):
			dic2[num] = i
			
		n = len(nums1)
		res = 0
		for i in range(n-2):
			
			for j in range(i+1,n-1):

				if dic2[nums1[j]] < dic2[nums1[i]] or dic2[nums1[j]] == n - 1: 
					continue
				else:
					left_list = nums1[:j]
					right_list = nums2[dic2[nums1[j]]+1:]
					print(left_list, right_list)
					res += len(set(left_list + right_list)) - len(left_list)
#				for k in range(j+1,n):
#					if dic2[nums1[k]] < dic2[nums1[j]] or dic2[nums1[k]] < dic2[nums1[i]]:
#						continue
#					res += 1
#					print(nums1[i], nums1[j], nums1[k])
		return res
# -------------------------
		
a = Solution()

b = [4,0,1,3,2]
c = [4,1,0,2,3]

b2 = [2,0,1,3]
c2 = [0,1,2,3]
print(a.goodTriplets(b2, c2))