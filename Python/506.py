#!/usr/bin/env python3
# 相对名次


from heapq import *
from typing import List,  Optional
from collections import defaultdict, deque
from itertools import product,combinations,permutations

class ListNode: 
	def __init__(self, val=0, next=None):
		self.val = val
		self.next = next

# -------------------------
class Solution:
	def findRelativeRanks(self, score: List[int]) -> List[str]:
		heap = []
		result = []
		for id, x in enumerate(score):
			heap.append([id, x])
		heap.sort(key = (lambda x:x[1]), reverse=True)
		for i,item in enumerate(heap):
			if i == 0:
				item.append("Gold Medal")
			elif i == 1:
				item.append("Silver Medal")
			elif i == 2:
				item.append("Bronze Medal")
			else:
				item.append(str(i + 1))
		

		heap.sort(key = (lambda x:x[0]), reverse=False)
		for i in heap:
			result.append(i[2])
		return result
		
		
# -------------------------
		
a = Solution()
b = [10,3,8,9,4]

print(Solution.findRelativeRanks(a, b))
