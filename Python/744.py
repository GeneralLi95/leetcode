#!/usr/bin/env python3
# @Date       : 2022/4/3 
# @Filename   : Untitled.txt
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
	def nextGreatestLetter(self, letters: List[str], target: str) -> str:		
		for lt in letters:
			if lt > target:
				return lt
		return letters[0]
# -------------------------
		
a = Solution()
l = ["c","f","j"]
tgt = 'a'
print(a.nextGreatestLetter(l, tgt))