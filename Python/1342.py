#!/usr/bin/env python3
# @Date       : 2022/1/31 
# @Filename   : 1342.py 将数字变成 0 的操作次数
# @Tag        : 位运算，数学
# @Autor      : LI YAO
# @Difficulty : Easy

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
	def numberOfSteps(self, num: int) -> int:
		ans = 0
		while num:
			ans += num & 1   # 与1 表示去最后一位，奇数的最后一位是1，偶数的最后一位是0
			if num > 1:
				ans += 1     # 加1 ，然后移位一次 
			num >>= 1
		return ans
	
		
# -------------------------
		
a = Solution()
b = 123
print(Solution.numberOfSteps(a, b))