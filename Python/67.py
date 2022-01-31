#!/usr/bin/env python3
# @Date       : 2022/1/31 
# @Filename   : 67.py
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
	def addBinary(self, a, b) -> str:	
		x, y = int(a, 2), int(b, 2)
		while y:     # 用 y 来保存进位，没有进位的时候即相加完成
			ans = x ^ y
			carry = (x & y) << 1   
			x , y = ans, carry
			print(bin(x)[2:], bin(y)[2:])    # 10进制数转二进制数会带个 0b [2:]去掉0b 
		return bin(x)[2:]
		
# -------------------------
		
slv = Solution()

print(slv.addBinary("1111", "10"))  