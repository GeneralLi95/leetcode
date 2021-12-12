#!/usr/bin/env python3
from typing import List
class Solution:
	def minimumRefill(self, plants: List[int], capacityA: int, capacityB: int) -> int:
		step = 0
		ca = capacityA

		cb = capacityB
		pb = len(plants)-1
		for i in range(len(plants)//2):
			if (plants[i] <= ca):
			
				ca = ca - plants[i]
				plants[i] = 0
			else:
				step = step + 1
				ca = capacityA - plants[i]
				plants[i] = 0
		for j in range(len(plants)//2):
			if (plants[-j-1] <= cb):
				
				cb = cb - plants[-j-1]
				plants[-j-1] = 0
			else:
				step = step + 1
				cb = capacityB - plants[-j-1]
				plants[-j-1] = 0
		print(plants, step)
		if (len(plants)%2 == 1):
			left = plants[len(plants)//2
			if max(ca,cb)<left:
				step = step +1
		return step
a = Solution()
b = [2,2,3,3]
b2 = [1,2,4,4,5]
b3= [7,7,7,7,7,7,7]

ca = 6
cb = 5
Solution.minimumRefill(a, b2, ca, cb)