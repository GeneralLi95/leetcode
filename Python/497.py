#!/usr/bin/env python3
# @Date       : 2022/1/16 ___TIME___
# @Filename   : 497.py
# @Tag        : 水塘抽样
# @Autor      : LI YAO
# @Difficulty : Medium

from heapq import *
from typing import List,  Optional
from collections import defaultdict, deque
from itertools import product,combinations,permutations
from random import choice, randrange

class ListNode: 
	def __init__(self, val=0, next=None):
		self.val = val
		self.next = next

# -------------------------
class Solution:
	
	def __init__(self, rects: List[List[int]]):
		self.rects = rects
		
	def pick(self) -> List[int]:
		result = []
		count = 0
		for rect in self.rects:
			x1, y1, x2, y2 = rect[0], rect[1], rect[2], rect[3]				
			area = (x2 - x1 + 1) * (y2 - y1 + 1)
			count += area    # 当前点的总数
			if randrange(count) < area:
				result = [randrange(x1, x2+1), randrange(y1,y2+1)]
		return result
		
# -------------------------
		
a = [[-2,-2,-1,-1],[1,0,3,0]]

obj = Solution(a)
print(obj.pick())