#!/usr/bin/env python3

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
	def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
		nums = len(arr)
		remove_num = nums - k
		
		while remove_num>0:
			if x - arr[0] <= arr[-1] - x:
				arr.pop(-1)
			else:
				arr.pop(0)
			remove_num -= 1
		return arr
		
		
# -------------------------
		
