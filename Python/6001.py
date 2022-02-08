#!/usr/bin/env python3
# @Date       : 2022/2/6 
# @Filename   : 6001.py
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
	def smallestNumber(self, num: int) -> int:		
		if num == 0:
			return num
		sn = list(str(num))
		n = len(sn)
		sn.sort()
		result = ['' for _ in range(n)]
		if sn[0] == '-':
			result[0] = '-'
			for i in range(1,n):
				result[i] = sn[n-i]
				
		elif sn[0] != '0':
			result = sn
		else:
			for i, num in enumerate(sn):
				if num != '0':
					sn[0], sn[i] = sn[i], sn[0]
					result = sn
					break


				
		res = ''
		for i in result:
			res += str(i)
		return int(res)
# -------------------------
		
a = Solution()
b = 0

print(a.smallestNumber(b))