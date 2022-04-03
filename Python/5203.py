#!/usr/bin/env python3
# @Date       : 2022/3/13 
# @Filename   : 5203.py
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
	def digArtifacts(self, n: int, artifacts: List[List[int]], dig: List[List[int]]) -> int:		
		n_art = len(artifacts)
		arts = [[] for _ in range(n_art)]
		for i in range(n_art):
			[x1,y1,x2,y2] = artifacts[i]
			for x in range(x1,x2+1):
				for y in range(y1,y2+1):
					arts[i].append([x,y])
		cnt = 0
		land = [[0 for _ in range(n)] for _ in range(n)] 
		for x,y in dig:
			land[x][y] = 1
		for i in arts:
			flag = True
			for x,y in i:
				if land[x][y] == 0:
					flag = False
					break
			if flag:
				cnt += 1

		return cnt
# -------------------------
		
a = Solution()

n1 = 2
artifacts1 = [[0,0,0,0],[0,1,1,1]]
dig1 = [[0,0],[0,1],[1,1]]

print(a.digArtifacts(n1, artifacts1, dig1))