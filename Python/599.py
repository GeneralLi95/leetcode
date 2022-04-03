#!/usr/bin/env python3
# @Date       : 2022/3/14 
# @Filename   : 599.py 两个列表的最小索引和
# @Tag        :
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
class Solution:
	def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
		dict1 = {}
		dict2 = {}
		
		for i, s in enumerate(list1):
			dict1[s] = i
		
		for i, s in enumerate(list2):
			dict2[s] = i
		
		result = defaultdict(list)
		min_res = 2001
		for name in dict1:
			if name in dict2:
				id = dict1[name] + dict2[name]
				min_res = min(id, min_res)
				result[id].append(name)
		
		return result[min_res]
		
		
# -------------------------
		
a = Solution()
l1 = ["Shogun", "Tapioca Express", "Burger King", "KFC"]
l2 = ["KFC", "Shogun", "Burger King"]
print(a.findRestaurant(l1, l2))