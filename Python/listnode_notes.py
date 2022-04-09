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

class ListNode: 
	def __init__(self, val=0, next=None):
		self.val = val
		self.next = next

first = ListNode(23)
first.next = ListNode(6)
first.next.next = ListNode(15)


cur = ListNode(9)
cur.next = first.next.next
first.next.next = cur

b = first
while b:
	if b.next.val == 9:
		b.next = b.next.next
		break
	
#print(first.val)   first 是不会动的