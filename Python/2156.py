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

# 正向滑动窗口，因为除法不满足取余的恒等性，所以无法做大数处理，导致超时
#class Solution:
#	def subStrHash(self, s: str, power: int, modulo: int, k: int, hashValue: int) -> str:		
#		n = len(s)
#		sum = 0
#		for i in range(k):
#			val = (ord(s[i]) - ord('a') + 1) * pow(power, i)
#			print('val=', val)
#			sum += val
#		if sum % modulo == hashValue:
#			return s[0:k]
#		print(sum)
#		for i in range(1, n-k+1):
#			sum = (sum - (ord(s[i-1]) - ord('a') + 1) )//power + (ord(s[i+k-1]) - ord('a') + 1) * pow(power, k-1)
#			print(sum)
#			if sum % modulo == hashValue:
#				return s[i:i+k]
	
#	class Solution:
#		def subStrHash(self, s: str, power: int, modulo: int, k: int, hashValue: int) -> str:
#			t = pow(power, k - 1, modulo)
#			val = ans = 0
#			for i in range(k):
#				val = (val + (ord(s[len(s) - 1 -i]) - ord('a') + 1) * pow(power, k - 1 - i, modulo) % modulo) % modulo
#			if val == hashValue:
#				ans = len(s) - k
#			for i in range(len(s) - 1, k - 1, -1):
#				val = (val - (ord(s[i]) - ord('a') + 1) * t % modulo) % modulo
#				val = val * power  % modulo
#				val = (val + ord(s[i - k]) - ord('a') + 1) % modulo 
#				if val == hashValue:
#					ans = i - k
#			return s[ans:ans+k]
		

# -------------------------
# 反向滑动窗口
class Solution:
	def subStrHash(self, s: str, power: int, modulo: int, k: int, hashValue: int) -> str:
		t = pow(power, k - 1, modulo)
		n = len(s)
		val = ans = 0
		for i in range(k):
			val = (val + (ord(s[n-i-1]) - ord('a') + 1) * pow(power, k - 1 - i, modulo) % module) % modulo   # 首项是高次
		
		if val == hashValue:
			ans = n - k
		
		for i in range(n, k -1, -1):
			
		
		
		
# -------------------------
		
a = Solution()
b = "leetcode"
p = 7
m = 20
k = 2
h = 0

print(a.subStrHash(b, p, m, k, h))