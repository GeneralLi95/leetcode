#!/usr/bin/env python3

from typing import List,  Optional
from collections import defaultdict, deque
from itertools import product,combinations,permutations

class ListNode: 
	def __init__(self, val=0, next=None):
		self.val = val
		self.next = next

# -------------------------
class Solution:
	def slowestKey(self, releaseTimes: List[int], keysPressed: str) -> str:
		
		n = len(releaseTimes)
		max_time = 0
		result = ''
		
		for i in range(n):
			if i == 0:
				time = releaseTimes[0]
				result = keysPressed[0]
			else:
				time = releaseTimes[i] - releaseTimes[i-1]
			if time > max_time:
				max_time = time
				result = keysPressed[i]
			elif time == max_time:
				result = max(result, keysPressed[i])
		return result
		
		
# -------------------------
		
a = Solution()
b = [9,29,49,50]
c = "cbcd"

b2 = [19,22,28,29,66,81,93,97]
c2 = "fnfaaxha"

b3 = [12,23,36,46,62]
c3 = "spuda"

print(Solution.slowestKey(a, b3, c3))