#!/usr/bin/env python3
# @Date       : 2022/3/6 
# @Filename   : 6018.py
# @Tag        :
# @Autor      : LI YAO
# @Difficulty :

from heapq import *
from typing import List,  Optional
from collections import defaultdict, deque, Counter
from itertools import product,combinations,permutations,accumulate
from random import choice, randrange,randint

class TreeNode:
	def __init__(self, val=0, left=None, right=None):
		self.val = val
		self.left = left
		self.right = right

# -------------------------
class Solution:
	def createBinaryTree(self, descriptions: List[List[int]]) -> Optional[TreeNode]:
		nodelist = {}
		root = []
		for i in descriptions:
			if i[0] not in root:
				root.append(i[0])
			if i[0] not in nodelist:
				node = TreeNode(i[0])
				nodelist[i[0]] = node
			if i[1] not in nodelist:
				node = TreeNode(i[1])
				nodelist[i[1]] = node

		for des in descriptions:
			if des[1] in root:
				root.remove(des[1])
			if des[2] == 1:
				nodelist[des[0]].left = nodelist[des[1]]
			else:
				nodelist[des[0]].right = nodelist[des[1]]
		
		return nodelist[root[0]]
		
		
		
# -------------------------
		
a = Solution()

d = [[20,15,1],[20,17,0],[50,20,1],[50,80,0],[80,19,1]]
a.createBinaryTree(d)

