#!/usr/bin/env python3
# @Date       : 2022/4/9 
# @Filename   : listnode_notes.py 链表学习记录
# @Tag        :
# @Autor      : LI YAO
# @Difficulty :

from heapq import *
from typing import List,  Optional
from collections import defaultdict, deque, Counter
from itertools import product,combinations,permutations,accumulate
from random import choice, randrange,randint


# 节点类
class ListNode: 
	def __init__(self, val=0, next=None):
		self.val = val
		self.next = next

		
# 链表类
class LinkedList:
	def __init__(self):
		self.headval = None	
		

list1 = LinkedList()
list1.headval = ListNode(23)
e2 = ListNode()
