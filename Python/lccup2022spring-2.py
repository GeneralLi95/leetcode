#!/usr/bin/env python3
# @Date       : 2022/4/16 
# @Filename   : lccup2022spring-2.py
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
	def perfectMenu(self, materials: List[int], cookbooks: List[List[int]], attribute: List[List[int]], limit: int) -> int:
		length = len(cookbooks)
		truth_table = set(product([0, 1], repeat=length))
		result = []

		for meal in truth_table:
			mt = materials[:]
			baofu = 0
			meiwei = 0
			for i in range(len(meal)):
				if meal[i] == 0:
					pass
				if meal[i] == 1:
					for j in range(5):
						mt[j] -= cookbooks[i][j]
					baofu += attribute[i][1]
					meiwei += attribute[i][0]
			if min(mt) >= 0 and baofu >= limit:
				result.append(meiwei)
		if len(result) > 0:
			return max(result)
		else:
			return -1
# -------------------------
		
a = Solution()

m1 = [10,10,10,10,10]
c1 = [[1,1,1,1,1],[3,3,3,3,3],[10,10,10,10,10]]
at1 = [[5,5],[6,6],[10,10]]
l1 = 1

m2 = [3,2,4,1,2]
c2 = [[1,1,0,1,2],[2,1,4,0,0],[3,2,4,1,0]]
at2 = [[3,2],[2,4],[7,6]]
l2 = 5
print(a.perfectMenu(m2, c2, at2, l2))
print(a.perfectMenu(m1, c1, at1, l1))