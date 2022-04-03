#!/usr/bin/env python3
# @Date       : 2022/2/19 
# @Filename   : 5998.py
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
	def maximumEvenSplit(self, finalSum: int) -> List[int]:
		res = []
		if finalSum % 2 == 1:
			return res
		i = 1
		while True:
			temp = 2 * i
			if finalSum - temp <= temp :
				res.append(finalSum)
				break
			else:
				res.append(temp)
				finalSum -= temp
				i += 1
				
		return res
# -------------------------
		
a = Solution()
b = 28
print(a.maximumEvenSplit(b))