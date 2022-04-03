#!/usr/bin/env python3
# @Date       : 2022/2/10 
# @Filename   : 1447.py 最简分数
# @Tag        :
# @Autor      : LI YAO
# @Difficulty :

from math import gcd
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
	def simplifiedFractions(self, n: int) -> List[str]:		
		res = []
		for i in range(2,n+1):
			for j in range(1,i):
				if gcd(i, j) == 1:
					res.append(f"{j}/{i}")
	
		return res
# -------------------------
		
a = Solution()
b = 6

print(a.simplifiedFractions(b))