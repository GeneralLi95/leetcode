#!/usr/bin/env python3
# @Date       : 2022/1/28 
# @Filename   : 1996.py
# @Tag        :
# @Autor      : LI YAO
# @Difficulty :

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
	def numberOfWeakCharacters(self, properties: List[List[int]]) -> int:	

		properties.sort(key=lambda x: (-x[0], x[1]))

		
		count = 0
		maxDef = 0
		for _, def_ in properties:
			if maxDef > def_:
				count += 1
			else:
				maxDef = max(maxDef, def_)
				
		return count
		

		
		
# -------------------------
		
a = Solution()
b = [[1,5],[10,4],[4,3],[2,7], [10,5]]
b2 = [[5,5],[6,3],[3,6]]
b3 =[[7,7],[1,2],[9,7],[7,3],[3,10],[9,8],[8,10],[4,3],[1,5],[1,5]]

Solution.numberOfWeakCharacters(a, b)