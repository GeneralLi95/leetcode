#!/usr/bin/env python3
# @Date       : 2022/1/18 
# @Filename   : 539.py 最小时间差
# @Tag        : 数组 字符串 排序
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
	def findMinDifference(self, timePoints: List[str]) -> int:
		time = [0 for _ in range(len(timePoints))]
		for i in range(len(timePoints)):
			time[i] = int(timePoints[i][0:2]) * 60 + int(timePoints[i][3:])
		time.sort()
		result = []
		for i in range(1, len(time)):
			result.append(time[i]-time[i-1])
		
		result.append(time[0] + 24*60 - time[-1])
		return min(result)
			
		
		
		
# -------------------------
		
a = Solution()
b = ["23:59","00:00"]
b2 = ["05:31","22:08","00:35"]

print(Solution.findMinDifference(a, b2))