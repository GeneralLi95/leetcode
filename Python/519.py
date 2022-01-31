#!/usr/bin/env python3
# @Date       : 2022/1/17 
# @Filename   : 519.py 随机翻转矩阵
# @Tag        : 水塘抽样
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
	
	def __init__(self, m: int, n: int):
		self.m = m
		self.n = n
		self.total = self.m * self.n
		self.map = {}
		
	def flip(self) -> List[int]:
		x = randint(0, self.total - 1)
		self.total -= 1
		# get 返回指定键的值，如果键不在字典中，则返回default
		# 如果该位置未被哈希表真实记录，则idx = x，
		# 这时因为这个点已经被用过了，所以需要找一个没有用过点取代他，就找最右端的点
		# 再把最右端的点total-1，左移一位，保证抽样区间的连续性
		# 太巧妙了这道题
		idx = self.map.get(x, x)        		
		self.map[x] = self.map.get(self.total, self.total)
		
		return [idx // self.n, idx % self.n]
		
		
	def reset(self) -> None:
		self.matrix = [[0] * self.n] * self.m
		self.total = self.m * self.n
		self.map.clear()  # 清空哈希表 字典清空
		
# -------------------------
		
a = 3
b = 1
obj = Solution(a, b)
param_1 = obj.flip()
obj.reset()