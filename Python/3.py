#!/usr/bin/env python3
# @Date       : 2022/2/12 
# @Filename   : 3.py 无重复字符的最长子串
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
	def lengthOfLongestSubstring(self, s: str) -> int:
		if len(s) == 0:
			return 0
		left = 0
		lookup = set()
		n = len(s)
		max_len = 0
		cur_len = 0
		for i in range(n):
			cur_len += 1
			while s[i] in lookup:
				lookup.remove(s[left])
				left += 1
				cur_len -= 1
			if cur_len > max_len : max_len = cur_len
			lookup.add(s[i])
		return max_len
		
		
# -------------------------
		
a = Solution()
b= "pwwkew"

a.lengthOfLongestSubstring(b)