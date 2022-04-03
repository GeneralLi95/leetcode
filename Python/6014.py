#!/usr/bin/env python3
# @Date       : 2022/2/20 
# @Filename   : 6014.py
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
	def repeatLimitedString(self, s: str, repeatLimit: int) -> str:		
		ls = list(s)
		ls.sort(reverse = True)
		dic = {}
		for key in ls:
			if key not in dic:
				dic[key] = 1
			else:
				dic[key] += 1
		print(dic)
		res = ''
		for i in range(15):
			flag = False
			for key, value in dic.items():
				if len(res) > 0 and res[-1] == key:

					continue
				if value == 0:
					flag = True
					continue
				if value <= repeatLimit:
					res += key * value
					dic[key] = 0
					flag = True
					break
				else:
					res += key * repeatLimit
					dic[key] -= repeatLimit
					break
				
				
		return res
# -------------------------
		
a = Solution()

b = "cczzzzzzzzzzazccaaaccc"
b1 = "aababab"
rl = 3
rl1 = 2
print(a.repeatLimitedString(b1, rl1))