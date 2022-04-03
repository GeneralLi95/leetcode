#!/usr/bin/env python3
# @Date       : 2022/3/30 
# @Filename   : 14.py
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
	def longestCommonPrefix(self, strs: List[str]) -> str:
		min_len = 200
		for ss in strs:
			min_len = min(min_len, len(ss))
		
		if len(strs) == 0:
			return ''
		if len(strs) == 1:
			return strs
		result = ''
		for i in range(min_len):
			flag = True
			for j in range(len(strs) - 1):
				if strs[j][i] != strs[j+1][i]:
					flag = False
					break
			if flag:
				result += strs[j][i]
			else:
				break
		return result
		
	
		
		
		
# -------------------------
		
a = Solution()
b = ["flower","flow","flight"]
print(a.longestCommonPrefix(b))