#!/usr/bin/env python3
# @Date       : 2022/4/10 
# @Filename   : 6037.py
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
	def largestInteger(self, num: int) -> int:
		s = str(num)
		jishu = defaultdict(int)
		oushu = defaultdict(int)
		for i, c in enumerate(s):
			if int(c) % 2 == 0:
				oushu[i] = int(c)
			else:
				jishu[i] = int(c)
		jishu_number = list(jishu.values())
		oushu_number = list(oushu.values())
		jishu_number.sort(reverse = True)
		oushu_number.sort(reverse = True)
		for i in jishu:
			jishu[i] = jishu_number[0]
			jishu_number.remove(jishu_number[0])
			
		for i in oushu:
			oushu[i] = oushu_number[0]
			oushu_number.remove(oushu_number[0])
		
		result = ''
		for i in range(len(s)):
			if i in jishu:
				result += str(jishu[i])
			else:
				result += str(oushu[i])
		return int(result)
		
		
# -------------------------
		
a = Solution()
b = 65875

print(a.largestInteger(b))