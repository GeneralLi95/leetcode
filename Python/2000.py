#!/usr/bin/env python3
# @Date       : 2022/2/2 
# @Filename   : 2000.py 反转单词前缀
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
	def reversePrefix(self, word: str, ch: str) -> str:		
		id = 0
		for i, ch_i in enumerate(word):
			if ch_i == ch:
				id = i
				break
		print(id)
		if id == 0:
			return word
		word = word[0:i+1][::-1] + word[i+1:len(word)]

		return word
		
# -------------------------
		
a = Solution()
b = "dcba"
c = "z"


print(a.reversePrefix(b, c))