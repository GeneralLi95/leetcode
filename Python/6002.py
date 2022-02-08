#!/usr/bin/env python3
# @Date       : 2022/2/6 
# @Filename   : 6002.py
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
class Bitset:
			
	def __init__(self, size: int):
		self.size = size
		self.bs = '0'* size
		self.flag = 0		
		
	def fix(self, idx: int) -> None:
		if self.bs[idx] == '1':
			return 
		else:
			self.flag += 1
			if idx == 0:
				self.bs = '1'+ self.bs[1:]
			elif idx == len(self.bs):
				self.bs = self.bs[0:len(self.bs)-1] + '1'
			else:
				self.bs = self.bs[0:idx] + '1' + self.bs[idx+1:]
		
		
	def unfix(self, idx: int) -> None:
		if self.bs[idx] == '0':
			return 
		else:
			self.flag -= 1
			if idx == 0:
				self.bs = '0'+ self.bs[1:]
			elif idx == len(self.bs):
				self.bs = self.bs[0:len(self.bs)-1] + '0'
			else:
				self.bs = self.bs[0:idx] + '0' + self.bs[idx+1:]

	
	def flip(self) -> None:

		self.flag = self.size - self.flag
		
		ls = list(self.bs)
		for i in range(len(ls)):
			if ls[i] == '0':
				ls[i] = '1'
		
			else:
				ls[i] = '0'
		
		self.bs = ''.join(ls)

	def all(self) -> bool:
		if self.flag == self.size:
			return True
		return False
			
	def one(self) -> bool:
		if self.flag >= 1:
			return True
		return False
#				
	def count(self) -> int:
		return self.flag
				
	def toString(self) -> str:
		return self.bs
				
		
		
# -------------------------
		
obj = Bitset(5)
obj.fix(3)
obj.fix(1)
print(obj.count())

obj.flip()
print(obj.toString())
print(obj.count())

obj.all()

obj.unfix(0)
print(obj.toString())
print(obj.count())
obj.flip()
print(obj.one())
obj.unfix(0)
print(obj.count())
print(obj.toString())

#param_4 = obj.all()
#param_5 = obj.one()
#param_6 = obj.count()
#param_7 = obj.toString()