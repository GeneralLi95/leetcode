#!/usr/bin/env python3
# @Date       : 12/2/22 
# @Filename   : 101.py 对称二叉树
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
	def isSymmetric(self, root):		
		if not root:
			return True
		def dfs(left, right):
			if not left and not right:  # 两个节点都是空
				return True
			if not left or not right:   # 有一个节点是空，一定不对称
				return False
			if left.val != right.val:  # 形状对称但是值不相等
				return False
			return dfs(left.left, right.right) and dfs(left.right, right.left)  # 注意下一个比较的对象
		return dfs(root.left, root.right)
		
		
# -------------------------
root1 = TreeNode(2)
root1.left = TreeNode(3)
root1.right = TreeNode(4)
root1.left.left = TreeNode(8)
root1.left.right = TreeNode(7)
root1.right.left = TreeNode(6)
root1.right.right = TreeNode(5)

root2 = TreeNode(1)
root2.left = TreeNode(2)
root2.right = TreeNode(2)
root2.left.left = TreeNode(3)
root2.left.right = TreeNode(4)
root2.right.left = TreeNode(4)
root2.right.right = TreeNode(3)


a = Solution()
print(a.isSymmetric(root1))
print(a.isSymmetric(root2))