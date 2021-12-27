#!/usr/bin/env python3
from typing import List
class Solution:
	def executeInstructions(self, n: int, startPos: List[int], s: str) -> List[int]:
		
		def point_in(n, pos: List[int]):
			if pos[0] < 0 or pos[1] <0:
				return False
			if pos[0] >= n or pos[1] >= n:
				return False
			return True

		result = []
		for i in range(len(s)):
			point_pos = startPos[:]
			j = i
			temp = 0
			while True:
				
				direct = s[j]
				if direct == "R":
					point_pos[1] += 1
				elif direct == "D":
					point_pos[0] += 1
				elif direct == "L":
					point_pos[1] -= 1
				elif direct == "U":
					point_pos[0] -= 1
				if point_in(n, point_pos):
					temp += 1
					j += 1
				else:
					break
				if j == len(s):
					break
			result.append(temp)
		return(result)
		
a = Solution()
b = 3
c = [0, 1]
d = "RRDDLU"

Solution.executeInstructions(a, b, c, d)