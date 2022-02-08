#!/usr/bin/env python3
# @Date       : 2022/2/5 
# @Filename   : 5986.py
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
	def minCostSetTime(self, startAt: int, moveCost: int, pushCost: int, targetSeconds: int) -> int:		
		target = 0
		if targetSeconds % 60 > 39:
			m1 = targetSeconds // 60 // 10  # 分钟 十位
			m2 = targetSeconds // 60 % 10  # 分钟  个位
			s1 = targetSeconds % 60 // 10  # 分钟  十位
			s2 = targetSeconds % 60 % 10  # 分钟   个位
			
			target = self.cal(startAt, moveCost,pushCost, m1,m2,s1,s2)
			return target
		
		if targetSeconds % 60 <= 39:
			m1 = targetSeconds // 60 // 10  # 分钟 十位
			m2 = targetSeconds // 60 % 10  # 分钟  个位
			s1 = targetSeconds % 60 // 10  # 分钟  十位
			s2 = targetSeconds % 60 % 10  # 分钟   个位
			
			
			m1x = (targetSeconds // 60 - 1) // 10
			m2x = (targetSeconds // 60 - 1) % 10
			s1x = (targetSeconds % 60 + 60) // 10
			s2x = (targetSeconds % 60 + 60 ) % 10
				
			target1 = self.cal(startAt, moveCost,pushCost, m1,m2,s1,s2)
			target2 = self.cal(startAt, moveCost, pushCost, m1x, m2x, s1x, s2x)
			
			if m1 >=  10:
				return target2
			
			if m1x >= 0:
				return min(target1, target2)
			else:
				return target1
			
	def cal(self, startAt, moveCost, pushCost, m1, m2, s1, s2):
		print(m1,m2,s1,s2)
		res = 0
		cur = startAt
		flag = 0
		for i, x in enumerate([m1,m2,s1,s2]):
			
			if i == 0 and x == 0:
				flag = 1
				continue
			if flag == 1 and x == 0:
				flag = 1
				continue 
			if x != cur:
				res = res + moveCost + pushCost
				cur = x
				flag = 0
			elif x == cur:
				res = res + pushCost
				flag = 0
		return res
				
# -------------------------
		
a = Solution()

s = 1
mc = 1
pc = 2
ts = 6008


print(a.minCostSetTime(s, mc, pc, ts))