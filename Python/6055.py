#!/usr/bin/env python3
# @Date       : 2022/4/3 
# @Filename   : 6055.py
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
	def convertTime(self, current: str, correct: str) -> int:
		total = (int(correct[0:2]) - int(current[0:2])) * 60 + (int(correct[3:]) - int(current[3:]))
		cnt = 0
		while total != 0:
			
			if total // 60 > 0:
				cnt += total // 60
				total = total % 60
				
			elif total // 15 > 0:
				cnt += total // 15
				total = total % 15
				
			elif total // 5 > 0:
				cnt += total // 5
				total = total % 5
			else:
				cnt += total
				total = 0
				
		return cnt
			
		
		
		
# -------------------------
		
a = Solution()
b = "02:30"
c = "04:35"
print(a.convertTime(b, c))