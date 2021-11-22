#!/usr/bin/env python3

class Solution:
	def maxDistance(self, colors: [int]) -> int:
		max_distance = 0
		for i in range(len(colors)):
			distance = 0
			if max_distance>(len(colors) - i):
				return max_distance
			for j in range(i, len(colors)):
				if colors[j]!=colors[i]:
					distance = (j-i)
				max_distance = max(max_distance, distance)
				
		return max_distance
		
a= Solution()
b = [1,1,1,6,1,1,1]
b2 = [0,1]
b3 = [1,8,3,8,3]
print(Solution.maxDistance(a, b3))