#!/usr/bin/env python3
# @Date       : 2022/1/22 
# @Filename   : 5974.py
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
	def numberOfWays(self, corridor: str) -> int:		
		count_s = corridor.count("S")
		if count_s ==0 or count_s % 2 !=0:
			return 0
		if count_s == 2:
			return 1
		count = 1
		seat = 0
		plant = 0
		for i in corridor:
			if i=="S" and seat != 2:
				seat += 1
				count_s -= 1
				continue
			if i=="P" and seat == 2 and count_s >= 2:
				plant += 1
				continue 

				
			if i=="S" and seat == 2 and count_s >= 2 and plant >0:
				count *= (plant +1) % (1e9+7)
				seat = 1
				count_s -= 1
				plant = 0
				continue
			if i =="S" and seat == 2:
				seat = 1

				
		return int(count % (1e9 +7))
				
		
		
# -------------------------
		
a = Solution()

c = "SSPPSPSPPPPP"
c2 = "PPSPSP"
c3 = "SPPSSSSPPS"
c4 = "SPSPPSSPSSSS"

print(Solution.numberOfWays(a, c3))