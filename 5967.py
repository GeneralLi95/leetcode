#!/usr/bin/env python3

class Solution:
	def checkString(self, s: str) -> bool:
		f = -1
		for i, c in enumerate(s):
			if c == "b":
				f = i
				break
		if f == -1:
			return True
		for j in range(f, len(s)):
			if s[j] == "a":
				return False
		return True

		
a = Solution()
b = "abab"
b2 = "bbb"
b3 = "aaabbb"
print(Solution.checkString(a, b3))