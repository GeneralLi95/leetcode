#!/usr/bin/env python3
# @Date       : 2022/6/12 
# @Filename   : 5259.py
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
	def calculateTax(self, brackets: List[List[int]], income: int) -> float:
		tax = 0
		former = 0
		for b in brackets:
			if income < b[0] - former:
				tax += income * b[1] / 100
				return tax
			else:
				tax += (b[0] - former) * b[1] / 100
				income = income + former - b[0]
				former = b[0]
				
		
			
				
		
		
# -------------------------
		
a = Solution()
b = [[3,50],[7,10],[12,25]]
c = 10
print(a.calculateTax(b, c))