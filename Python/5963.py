#!/usr/bin/env python3

class Solution:
	def isSameAfterReversals(self, num: int) -> bool:
		if num == 0:
			return True
		if num % 10 == 0  :
			return False
		return True
a = Solution()
b = 526
print(Solution.isSameAfterReversals(a, b))