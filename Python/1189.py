#!/usr/bin/env python3
# @Date       : 2022/2/13 
# @Filename   : 1189.py
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
	def maxNumberOfBalloons(self, text: str) -> int:		
		tt = Counter(text)
		ba = ['b','a','l','o','n']
		res = 2000
		for ch in ba:
			if ch != 'l' and ch != 'o':
				res = min(res, tt[ch])
			else:
				res = min(res, tt[ch] // 2)
		return res
		
# -------------------------
		
a = Solution()
b = "loonbalxballpoon"
b2 = "balon"
print(a.maxNumberOfBalloons(b2))