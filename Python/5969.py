#!/usr/bin/env python3
from typing import List
class Solution:
	def asteroidsDestroyed(self, mass: int, asteroids: List[int]) -> bool:
		asteroids.sort()
		print(asteroids)
		for i in asteroids:
			if mass >= i:
				mass += i
			else:
				return False
		return True
a = Solution()
b = 10
c = [3,9,19,5,21]
b2 = 5
c2 = [4,9,23,4]
print(Solution.asteroidsDestroyed(a, b2, c2))