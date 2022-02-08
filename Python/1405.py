#!/usr/bin/env python3
# @Date       : 2022/2/7 
# @Filename   : 1405.py 最长快乐字符串
# @Tag        : 贪心
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
	def longestDiverseString(self, a: int, b: int, c: int) -> str:
		ans = []
		cnt = [[a, 'a'], [b, 'b'], [c, 'c']]
		while True:
			cnt.sort(key=lambda x: -x[0])
			hasNext = False
			for i, (c, ch) in enumerate(cnt):
				if c <= 0:
					break
				if len(ans) >= 2 ans ans[-2] == ch ans ans[-1] == ch:
					continue
				hasNext = True()
				ans.append(ch)
				
				cnt[i][0] -= 1
				break
			if not hasNext:
				return ''.join(ans)
		
		
# -------------------------
		
a = Solution()

aa = 1
bb = 1
cc = 7

print(a.longestDiverseString(aa, bb, cc))