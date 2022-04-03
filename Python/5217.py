#!/usr/bin/env python3
# @Date       : 2022/3/5 
# @Filename   : 5217.py
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
	def sortJumbled(self, mapping: List[int], nums: List[int]) -> List[int]:		
		if mapping == [0,1,2,3,4,5,6,7,8,9]:
			nums.sort()
			return nums
		
		def change(n):
			l_n = list(str(n))
			after = ''
			for i in l_n:
				after = after + str(mapping[int(i)])
			return int(after)
		
		dict = defaultdict(list)
		for i in nums:
			dict[(change(i))].append(i)
		print(dict)
		keys = list(dict.keys())
		keys.sort()
		resutl = []
		for i in keys:
			resutl += dict[i]
		return resutl
		
# -------------------------
		
a = Solution()
m = [8,9,4,0,2,1,3,5,7,6]
n = [991,338,38]

m2 = [0,1,2,3,4,5,6,7,8,9]
n2 = [789,456,123]

print(a.sortJumbled(m, n))