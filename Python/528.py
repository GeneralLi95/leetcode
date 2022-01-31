#!/usr/bin/env python3
# @Date       : 2022/1/17 ___TIME___
# @Filename   : 528.py 按权重随机生成点
# @Tag        : 
# @Autor      : LI YAO
# @Difficulty : Medium

from heapq import *
from typing import List,  Optional
from collections import defaultdict, deque
from itertools import product,combinations,permutations,accumulate
from random import choice, randrange, randint
from bisect import bisect_left

class ListNode: 
	def __init__(self, val=0, next=None):
		self.val = val
		self.next = next

# -------------------------
# 普通水塘抽样
#class Solution:
#	
#	def __init__(self, w: List[int]):
#		self.w = w
#		
#	def pickIndex(self) -> int:
#		count = 0
#		result = 0
#		for id, x in enumerate(self.w):
#			count += x
#			if randrange(count) < x:
#				result = id
#		return result
#		
# -------------------------
# 带二分法 + 前缀和
class Solution:
	
	def __init__(self, w: List[int]):
		self.pre = list(accumulate(w))  # 前缀和矩阵
		self.total = sum(w)
		
	
	def pickIndex(self) -> int:
		x = randint(1, self.total)
		return bisect_left(self.pre, x)
		
# -------------------------
		
a = [1, 3]
obj = Solution(a)
print(obj.pickIndex())