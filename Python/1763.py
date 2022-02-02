#!/usr/bin/env python3
# @Date       : 2022/2/1 
# @Filename   : 1763.py 最长的美好子字符串
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
	def longestNiceSubstring(self, s: str) -> str:	
		n = len(s)
		if n == 1:
			return ""
		result = defaultdict(list)
		for i in range(n):
			for j in range(i+1,n+1):
				sbs = list(set(s[i:j]))
				print(sbs)
				if len(sbs) == 2 and abs(ord(sbs[0]) - ord(sbs[1])) == 32:
					print(sbs)
					result[j-i].append(s[i:j])
		if len(result) == 0:
			return ""
		return result[max(result)][0]
					
	
		
		
# -------------------------
		
a = Solution()
b = "YazaAay"
b2 = "jcJ"
a.longestNiceSubstring(b2)