#!/usr/bin/env python3
# @Date       : 2022/2/5 
# @Filename   : 1219.py
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
	def getMaximumGold(self, grid: List[List[int]]) -> int:		
		m, n = len(grid), len(grid[0])
		ans = 0
		
		def dfs(x: int, y: int, gold: int) -> None:
			gold += grid[x][y]
			nonlocal ans
			ans = max(ans, gold)
			
			rec = grid[x][y]
			grid[x][y] = 0
			
			for nx, ny in ((x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)):
				if 0 <= nx < m and 0 <= ny < n and gird[nx][ny] > 0 :
					dfs(nx, ny, gold)
					
			grid[x][y] = rec 
			
		for i in range(m):
			for j in range(n):
				if grid[i][j] != 0 :
					dfs(i, j, 0)
					
		return ans 
		
# -------------------------
		
a = Solution()