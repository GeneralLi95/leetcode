#!/usr/bin/env python3
# @Date       : 2022/4/10 
# @Filename   : 6039.py
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
	def maximumProduct(self, nums: List[int], k: int) -> int:

		c = Counter(nums)
		c = dict(c)
		key_list = list(c.keys())
		key_list.sort()
		print(c)
		print(key_list)
		for i in range(len(key_list)-1):
			if k > (c[key_list[i+1]] - c[key_list[i]]) * key_list[i]:
				c[key_list[i+1]] += c[key_list[i]]
				c[key_list[i]] = 0
				print(c)
			else:
				if k < c[key_list[i]]:
					c[key_list[i]] -= k
					c[key_list[i] + 1] += k
				else:
					temp1 = k // c[key_list[i]]
					temp2 = k % c[key_list[i]]
					c[key_list[i] + temp1] += (c[key_list[i]] - temp2)
					c[key_list[i] + temp1 + 1] += temp2
					c[key_list[i]] = 0

				k = 0
			if k == 0:
				break
		print(c)
			
		res = 1
		for i, num in c.items():
			if num != 0 :
				res = res * i ** num
			
		return res % (1e9 + 7)
		
		
# -------------------------
		
a = Solution()
b1 = [6,3,3,2]
k1 = 2
b2 = [0,4]
k2 = 5
b3=[24,5,64,53,26,38]
k3=54

print(a.maximumProduct(b3, k3))



# 180820950