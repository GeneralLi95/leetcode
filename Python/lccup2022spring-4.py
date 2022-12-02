#!/usr/bin/env python3
# @Date       : 2022/4/16 
# @Filename   : lccup2022spring-4.py
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
	def defendSpaceCity(self, time: List[int], position: List[int]) -> int:
		attck = defaultdict(list)
		for i in range(len(time)):
			attck[time[i]].append(position[i])
		attck_time = set(time)
		status = [0] * max(position)
		energy = 0
		for i in range(max(time)+1):
			if i not in attck_time:
				status = [0] * max(position)
			if i in attck_time:
				need_proctect = attck[i]
				need_proctect.sort()
				print(need_proctect)
			
		
# -------------------------
		
a = Solution()

t1 = [1,2,1]
p1 = [6,3,3]

t2 = [1,1,1,2,2,3,5]
p2 = [1,2,3,1,2,1,3]

print(a.defendSpaceCity(t2, p2))