#!/usr/bin/env python3
# @Date       : 12/2/22 
# @Filename   : 112.py 路径总和，判断二叉树里是否存在指定长度的路径
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
class Solution(object):
	def hasPathSum(self, root, sum):
		if not root: return False
		if not root.left and not root.right:
			return sum == root.val
		return self.hasPathSum(root.left, sum - root.val) or self.hasPathSum(root.right, sum - root.val)  # sum 在这里不断更新，这个递归很巧妙
		
# -------------------------
		
a = Solution()