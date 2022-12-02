#!/usr/bin/env python3
# @Date       : 12/2/22 
# @Filename   : 102.py 二叉树层序遍历
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

class TreeNode:
	def __init__(self, val=0, left=None, right=None):
		self.val = val
		self.left = left
		self.right = right
# -------------------------
class Solution:
	def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
		result = []
		q = deque()
		if root:
			q.append(root)
		while q:
			node_list = []
			for i in range(len(q)):
				node = q.popleft()
				node_list.append(node.val)
				if node.left:
					q.append(node.left)
				if node.right:
					q.append(node.right)
			result.append(node_list)
		return result		
		
		
# -------------------------
		
a = Solution()