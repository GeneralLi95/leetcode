#!/usr/bin/env python3
from collections import defaultdict
class Solution:
	def countPoints(self, rings: str) -> int:
		dict = defaultdict(str)
		for i in range(len(rings)//2):
			key = int(rings[i*2+1])
			value = rings[i*2]
			print(key,value)
			dict[key] = dict[key]+value
#			result[int(rings[i*2+1])].append(rings[i*2])
			print(dict)
		result = 0
		for i in dict:
			if len(set(dict[i]))==3:
				result += 1
		return result
a = Solution()
b = "B0B6G0R6R0R6G9"
Solution.countPoints(a, b)