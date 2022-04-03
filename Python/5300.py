#!/usr/bin/env python3
# @Date       : 2022/3/5 
# @Filename   : 5300.py
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
	def getAncestors(self, n: int, edges: List[List[int]]) -> List[List[int]]:		
		dict = defaultdict(list)
		for e in edges:
			dict[e[1]].append(e[0])
		print(dict)
		result = [[] for _ in range(n)]
		print(result)

		def bfs(i):
			ans = dict[i]
			if i not in dict:
				return 
			if i in dict:
				for j in dict[i]:
					ans += bfs(j)
					ans = list(set(ans))
			return ans
		

		for i in range(n):
			if i not in dict:
				continue
			else:
				result[i] = bfs(i)
				result[i].sort()
		return result

			
			
#		for i, anc in dict.items():
#			stack = anc[:]
#			while stack != []:
#				if i not in dict:
#					stack.
					
# -------------------------
		# defaultdict(<class 'list'>, {3: [0, 1], 4: [0, 2], 7: [2, 3], 5: [3], 6: [3, 4]})
a = Solution()

n1 = 8
el1 = [[0,3],[0,4],[1,3],[2,4],[2,7],[3,5],[3,6],[3,7],[4,6]]

n2 = 5
el2 =  [[0,1],[0,2],[0,3],[0,4],[1,2],[1,3],[1,4],[2,3],[2,4],[3,4]]

print(a.getAncestors(n1, el1))