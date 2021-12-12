#!/usr/bin/env python3
from typing import List
from collections import defaultdict, deque
from itertools import product,combinations,permutations
class Solution:
	def findEvenNumbers(self, digits: List[int]) -> List[int]:
				
		temp =  list(set(permutations(digits,3)))
		result = []
		for i in temp:
			if i[0] == 0 or (i[2]%2 != 0):
				continue
			result.append(i[0]*100 + i[1]*10 + i[2])
		result.sort()
		return result
		
a = Solution()
b = [2,1,3,0]
print(Solution.findEvenNumbers(a, b))