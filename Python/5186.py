#!/usr/bin/env python3
# 区间内查询数字的频率


class RangeFreqQuery:
	
	def __init__(self, arr: [int]):
		self.arr = arr
		return None
		
	def query(self, left: int, right: int, value: int) -> int:
				
		return self.arr[left:right+1].count(value)
	
		
a = RangeFreqQuery([12, 33, 4, 56, 22, 2, 34, 33, 22, 12, 34, 56])

print(RangeFreqQuery.query(a, 0, 11, 33))