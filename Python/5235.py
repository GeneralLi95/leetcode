#!/usr/bin/env python3
# @Date       : 2022/4/3 
# @Filename   : 5235.py
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
	def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
		play_dict = defaultdict()
		for game in matches:
			if game[0] not in play_dict:
				play_dict[game[0]] = 0
			if game[1] not in play_dict:
				play_dict[game[1]] = 1
			else:
				play_dict[game[1]] += 1
		
		result_win = []
		result_lose = []
		for i, num in play_dict.items():
			if num == 0:
				result_win.append(i)
			elif num == 1:
				result_lose.append(i)
		return [sorted(result_win), sorted(result_lose)]
		
		
		
# -------------------------
		
a = Solution()

m = [[1,3],[2,3],[3,6],[5,6],[5,7],[4,5],[4,8],[4,9],[10,4],[10,9]]

print(a.findWinners(m))