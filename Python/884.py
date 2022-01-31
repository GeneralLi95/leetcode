#!/usr/bin/env python3
# @Date       : 2022/1/30 
# @Filename   : 884.py
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
		def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:		
			freq = Counter(s1.split()) + Counter(s2.split())
			print(freq)
			ans = []
			for word, occ in freq.items():
				if occ == 1:
					ans.append(word)
					
			return ans
		
		
# -------------------------
		
a = Solution()

b1 = "this apple is sweet"
b2 = "this apple is sour"

print(Solution.uncommonFromSentences(a, b1, b2))