#!/usr/bin/env python3
# @Date       : 2022/2/27 
# @Filename   : 6010.py
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
	def minimumTime(self, time: List[int], totalTrips: int) -> int:		
		if len(time) == 1:
			return totalTrips * time[0] 
		time.sort()
		bus = {}
		for i in time:
			if i not in bus:
				bus[i] = 1
			else:
				bus[i] += 1
			
		def is_bigger(time_stamp):
			result = 0
			for bus_id, num in bus.items():
				result += time_stamp // bus_id * num
				if result >= totalTrips:
					return True
			return False
		
		right = 10000000000000
		left = 0
		while left < right -1 :
			mid = (left + right) // 2
			if is_bigger(mid):
				right = mid
			else:
				left = mid
		return right
				
# -------------------------
		
a = Solution()

t = [1,2,3]
total = 5
t1 = [2]
total1 = 1
t2 = [5, 10, 10]
total2 = 9
print(a.minimumTime(t2,total2))