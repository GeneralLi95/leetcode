#!/usr/bin/env python3

# 植物浇水

class Solution:
	def wateringPlants(self, plants: [int], capacity: int) -> int:
		step = 0
		cc = capacity
		for i in range(len(plants)):
			if (plants[i] <= cc):
				step += 1
				cc = cc - plants[i]
			else:
				step = step + i*2 + 1
				cc = capacity - plants[i]
		return step
		
a = Solution()
b = [2,2,3,3]
b2 = [1,1,1,4,2,3]
b3= [7,7,7,7,7,7,7]

c = 5
c2 = 4
c3 = 8
print(Solution.wateringPlants(a, b3, c3))


