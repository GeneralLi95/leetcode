#!/usr/bin/env python3
# @Date       : 2022/1/27 
# @Filename   : 2047.py 句子有效单词数
# @Tag        :
# @Autor      : LI YAO
# @Difficulty :

from heapq import *
from typing import List,  Optional
from collections import defaultdict, deque
from itertools import product,combinations,permutations,accumulate
from random import choice, randrange,randint
import re


class ListNode: 
	def __init__(self, val=0, next=None):
		self.val = val
		self.next = next

# -------------------------
class Solution:
	def countValidWords(self, sentence: str) -> int:
		words = sentence.split()
		print(words)
		count = 0
		for word in words:
			flag = False
			hasHyphens = False
			for i, ch in enumerate(word):
				if ch.isdigit() or ch in "!.," and i <len(word) - 1:
					flag = False
					break
				if ch == '-':
					if hasHyphens or i == 0 or i == len(word) - 1 or not word[i-1].islower() or not word[i+1].islower():
						flag = False
						break
					hasHyphens = True
				flag = True
			if flag:
				count += 1
		return count
# -------------------------
		
a = Solution()
b = "he bought 2 pencils, 3 erasers, and 1  pencil-sharpener."
b2 = "!this  1-s b8d!"

print(Solution.countValidWords(a, b))