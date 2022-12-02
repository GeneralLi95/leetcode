#!/usr/bin/env python3
# @Date       : 2022/4/17 
# @Filename   : 6072.py
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
	def maxTrailingZeros(self, grid: List[List[int]]) -> int:
		
		def cnt_zero(ll):
			zero_number = 0
			result = 1
			for i in ll:
				result *= i
			temp_s = str(result)
			temp_s2 = temp_s.rstrip('0')
			zero_number = len(temp_s) - len(temp_s2)


			return zero_number
		
				
		m = len(grid)
		n = len(grid[0])

		result = 0
		for i in range(m):
			for j in range(n):
				if grid[i][j] % 10 == 0 or grid[i][j] % 5 == 0:
					
					ls1 = grid[i]
					ls2 = [grid[p][j] for p in range(m)]
					
					ls3 = grid[i][:j] + [grid[p][j] for p in range(0,i)]
					print(grid[i][j],ls3)
					ls4 = grid[i][j:] +[grid[p][j] for p in range(1,i)]
					
					ls5 = grid[i][:j] + [grid[p][j] for p in range(i+1,m)]
					ls6 = grid[i][j:] +[grid[p][j] for p in range(i+1,m)]
#					print(ls6,cnt_zero(ls6))
					result = max(result,cnt_zero(ls1))
					result = max(result,cnt_zero(ls2))
					result = max(result,cnt_zero(ls3))
					result = max(result,cnt_zero(ls4))
					result = max(result,cnt_zero(ls5))
					result = max(result,cnt_zero(ls6))
#							
		return result
							
# -------------------------
							
a = Solution()

g = [[23,17,15,3,20],[8,1,20,27,11],[9,4,6,2,21],[40,9,1,10,6],[22,7,4,5,3]]


g2 = [[1,15,2,4,25]]

print(a.maxTrailingZeros(g2))

