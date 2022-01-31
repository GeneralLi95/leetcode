#!/usr/bin/env python3
# @Date       : 2022/1/23 
# @Filename   : 2034.py 股票价格波动
# @Tag        :
# @Autor      : LI YAO
# @Difficulty :

from heapq import *
from typing import List,  Optional
from collections import defaultdict, deque
from itertools import product,combinations,permutations,accumulate
from random import choice, randrange,randint
from sortedcontainers import SortedList

class ListNode: 
	def __init__(self, val=0, next=None):
		self.val = val
		self.next = next

# -------------------------
class StockPrice:
	
	def __init__(self):
		self.stock = {}
		self.price = SortedList() # 有序列表
		self.maxTimestamp = 0 # 维护一个时间戳
		
	def update(self, timestamp: int, price: int) -> None:
		if timestamp in  self.stock:
			self.price.discard(self.stock[timestamp])    # discard 有序列表删除
		self.price.add(price)
		self.stock[timestamp] = price
		self.maxTimestamp = max(self.maxTimestamp,timestamp)

	def current(self) -> int:
		return self.stock[self.maxTimestamp]
#		
#			
	def maximum(self) -> int:
		return self.price[-1]
#			
	def minimum(self) -> int:
		return self.price[0]
		
		
		
# -------------------------
		
obj = StockPrice()
obj.update(2,20)
obj.update(1,5)
obj.update(3,7)
obj.update(3,6)
print(obj.current())
print(obj.maximum())
print(obj.minimum())