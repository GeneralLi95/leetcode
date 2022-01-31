#!/usr/bin/env python3
# @Date       : 2022/1/26 
# @Filename   : 2013.py 
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

class DetectSquares:
	
	def __init__(self):
		self.map = defaultdict(Counter)     # Counter 计数类
		
		
	def add(self, point: List[int]) -> None:
		x , y = point
		self.map[y][x] += 1   # 双重哈希 
		
		
	def count(self, point: List[int]) -> int:
		res = 0
		x, y = point
		
		if not y in self.map :
			return 0
		
		yCnt = self.map[y]
		
		for col, colCnt in self.map.items():
			if col != y:
				d = col - y
				res += colCnt[x] * yCnt[x + d] * colCnt[x + d]
				res += colCnt[x] * yCnt[x - d] * colCnt[x - d]
		return res
		
		
		
# -------------------------
		
obj = DetectSquares()
obj.add([3,10])
obj.add([11,2])
obj.add([3,2])
obj.count([11,10])
obj.count([14,8])

obj.add([11,2])
obj.count([11,10])


