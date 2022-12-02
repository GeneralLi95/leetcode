#!/usr/bin/env python3
# @Date       : 2022/4/16 
# @Filename   : 6062.py   ATM
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
class ATM:
			
	def __init__(self):
		self.money_20 = 0
		self.money_50 = 0
		self.money_100 = 0
		self.money_200 = 0
		self.money_500 = 0
				
				
	def deposit(self, banknotesCount: List[int]) -> None:
		self.money_20 += banknotesCount[0]
		self.money_50 += banknotesCount[1]
		self.money_100 += banknotesCount[2]
		self.money_200 += banknotesCount[3]
		self.money_500 += banknotesCount[4]
		print("now have")
		print([self.money_20, self.money_50, self.money_100, self.money_200, self.money_500])
		print()
				
	def withdraw(self, amount: int) -> List[int]:		
		money_dict = {500:self.money_500,200:self.money_200,100: self.money_100,50: self.money_50,20: self.money_20}
		result = []
		for mianzhi, number in money_dict.items():
			if amount < mianzhi:
				result.append(0)
				continue
			else:
				needed = amount // mianzhi
				taked = min(needed, number)
				result.append(taked)
				amount = amount - taked*mianzhi

		if amount == 0:
			self.money_500 -= result[0]
			self.money_200 -= result[1]
			self.money_100 -= result[2]
			self.money_50 -= result[3]
			self.money_20 -= result[4]
			return result[::-1]
		else:
			return -1
# -------------------------
		
atm = ATM()
atm.deposit([0,0,1,2,1])
print(atm.withdraw(600))
atm.deposit([0,1,0,1,1])
					
print(atm.withdraw(600))      
												
print(atm.withdraw(550))