#!/usr/bin/env python3
# @Date       : 2022/2/14 
# @Filename   : 733.py 图像渲染
# @Tag        : 广度优先搜索，深度优先搜索
# @Autor      : LI YAO
# @Difficulty : Easy

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
#class Solution:
#	def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:	
#		if newColor == image[sr][sc]:
#			return image
#		
#		directions = {(1,0), (-1,0), (0,1), (0,-1)}
#		
#		# 构造一个队列，先把初始点放进去
#		que = deque()
#		que.appendleft((sr,sc))
#		
#		# 记录初始颜色
#		originalcolor = image[sr][sc]
#		
#		# 当队列不为空
#		while que:
#			point = que.pop()
#			image[point[0]][point[1]] = newColor
#			# 遍历四个方向
#			for direction in directions:
#				# 新点是(new_i,new_j)
#				new_point = (point[0] + direction[0], point[1] + direction[1])
#				if new_point[0] in  range(len(image)) and new_point[1] in range(len(image[0])) and image[new_point[0]][new_point[1]] == originalcolor:
#					# 这是一个很关键的判断条件，必须要等于 originalcolor 才能加进去，已经被染色的或者 0 都不能加进去
#					que.appendleft(new_point)
#		return image
		
		
# -------------------------
class Solution:
	def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:	
		if newColor == image[sr][sc]:
			return image
#		构造一个栈，把初始点放进去
		stack = [(sr,sc)]

		originalcolor = image[sr][sc]
		
		while stack:
			point = stack.pop()
			image[point[0]][point[1]] = newColor
			for new_point in zip((point[0], point[0], point[0] + 1, point[0] - 1), (point[1] + 1, point[1] - 1, point[1], point[1])): 
				if new_point[0] in range(len(image)) and new_point[1] in range(len(image[0])) and image[new_point[0]][new_point[1]] == originalcolor:
					stack.append(new_point)
		return image

	
	
# -------------------------
		
a = Solution()

img = [[1,1,1],[1,1,0],[1,0,1]]

sr1 = 1
sc1 = 1
nc = 2

print(a.floodFill(img, sr1, sc1, nc))