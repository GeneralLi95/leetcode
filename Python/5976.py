#!/usr/bin/env python3

from typing import List

class Solution:
	def checkValid(self, matrix: List[List[int]]) -> bool:
		n = len(matrix)
		print(matrix)
		transposed = []

		for i in range(n):
			if len(set(matrix[i])) !=n :
				return False
			r = []
			for j in matrix:
				if j[i] in r:
					return False
				r.append(j[i])
			transposed.append(r)
		return True
	
a = Solution()
b = [[1,1,1],[1,2,3],[1,2,3]]
b2 = [[1,2,3],[3,1,2],[2,3,1]]
print(Solution.checkValid(a, b))