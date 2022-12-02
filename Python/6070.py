#!/usr/bin/env python3
# @Date       : 2022/4/17 
# @Filename   : 6070.py
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
	def digitSum(self, s: str, k: int) -> str:
		while len(s) > k:
			temp_s = ''
			if len(s) % k == 0:
				length = len(s) // k
			else:
				length = len(s) // k + 1
			for i in range(length):
				temp = 0
				for j in s[i*k:i*k+k]:
					temp += int(j)
				temp_s += str(temp)
			s = temp_s
		return s
		
		
# -------------------------
		
a = Solution()
s1 = "11111222223"
k1 = 3

s2 = "1234"
k2 = 2

# 37
print(a.digitSum(s1, k1))