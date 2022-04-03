#!/usr/bin/env python3
# @Date       : 2022/2/14 
# @Filename   : 695.py 岛屿最大面积
# @Tag        : 广度优先搜索，深度优先搜索
# @Autor      : LI YAO
# @Difficulty : Medium

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

		
		
		
	def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
		m = len(grid)
		n = len(grid[0])
	
		que = deque()
		flag_dic = {}
		

				
					
		print(cnt_area)
			
			
		
		
		
# -------------------------
		
a = Solution()

g = [[0,0,1,0,0,0,0,1,0,0,0,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,1,1,0,1,0,0,0,0,0,0,0,0],[0,1,0,0,1,1,0,0,1,0,1,0,0],[0,1,0,0,1,1,0,0,1,1,1,0,0],[0,0,0,0,0,0,0,0,0,0,1,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,0,0,0,0,0,0,1,1,0,0,0,0]]

print(a.maxAreaOfIsland(g))
