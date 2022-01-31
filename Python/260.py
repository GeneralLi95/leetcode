#!/usr/bin/env python3
# @Date       : 2022/1/31 
# @Filename   : 260.py 只出现一次的数字III   这次这个数字有两个
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
	def singleNumber(self, nums: List[int]) -> List[int]:		
		xorsum = 0
		for num in nums:
			xorsum ^= num
		
		print(bin(-xorsum))
				
		lsb = xorsum & (-xorsum)   # 负数的二进制码是其对应正数的按位取反加1
		print(lsb)
		type1 = type2 = 0
		r1 = []
		r2 = []
		for num in nums:
			if num & lsb:
				r1.append(num)
				type1 ^= num
			else:
				r2.append(num)
				type2 ^= num
		print(r1,r2)
		return [type1, type2]
# -------------------------
		
a = Solution()
b = [1,1, 2, 3, 5, 2, 4,4]
print(a.singleNumber(b))