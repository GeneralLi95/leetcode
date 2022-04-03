#!/usr/bin/env python3
# @Date       : 2022/3/6 
# @Filename   : 6016.py
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
	def cellsInRange(self, s: str) -> List[str]:		
		result = []
		ss = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
		ls = list(ss)
		dict = {}
		cnt = 0
		for c in ls:
			dict[c] = cnt 
			cnt += 1
		left = s[0]
		right = s[3]
		num1 = int(s[1])
		num2 = int(s[4])
		
		for i in range(dict[left],dict[right]+1):
			for j in range(num1, num2+1):
				result.append(ls[i] + str(j) )
		return result
# -------------------------
		
a = Solution()
s1 = "K1:L2"

print(a.cellsInRange(s1))