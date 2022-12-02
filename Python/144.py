#!/usr/bin/env python3
# @Date       : 12/2/22 
# @Filename   : 144.py 二叉树的前序遍历
# @Tag        :
# @Autor      : LI YAO
# @Difficulty :

from heapq import *
from typing import List,  Optional
from collections import defaultdict, deque, Counter
from itertools import product,combinations,permutations,accumulate
from random import choice, randrange,randint

#class ListNode: 
#	def __init__(self, val=0, next=None):
#		self.val = val
#		self.next = next
#
class TreeNode:
	def __init__(self, val=0, left=None, right=None):
		self.val = val
		self.left = left
		self.right = right
# -------------------------
class Solution:
	def preorderTraversal(self, root: TreeNode) -> List[int]:
		if not root:
			return []
		return [root.val] + self.preorderTraversal(root.left) + self.preorderTraversal(root.right)		
		
		
# -------------------------
rootnode = TreeNode(1)
rootnode.right = TreeNode(2)
rootnode.right.left = TreeNode(3)
a = Solution()
print(a.preorderTraversal(rootnode))