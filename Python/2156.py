#!/usr/bin/env python3
# @Date       : 2022/2/2 
# @Filename   : 2156.py
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
	def subStrHash(self, s: str, power: int, modulo: int, k: int, hashValue: int) -> str:		
		n = len(s)
		sum = 0
		for i in range(k):
			val = (ord(s[i]) - ord('a') + 1) * pow(power, i)
			print('val=', val)
			sum += val
		if sum % modulo == hashValue:
			return s[0:k]
		print(sum)
		for i in range(1, n-k+1):
			sum = (sum - (ord(s[i-1]) - ord('a') + 1) )//power + (ord(s[i+k-1]) - ord('a') + 1) * pow(power, k-1)
			print(sum)
			if sum % modulo == hashValue:
				return s[i:i+k]
			
		
# -------------------------
		
a = Solution()
b =  "leetcode"
p = 7
m = 20
k = 2
h = 0

print(a.subStrHash(b, p, m, k, h))