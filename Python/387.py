#!/usr/bin/env python3

class Solution:
	def firstUniqChar(self, s: str) -> int:
		
		a = list(set(s))
		a.sort(key = s.index)
		
		for c in a:

			if s.count(c) == 1:
				return s.find(c)
		return -1
	

a = Solution()
print(Solution.firstUniqChar(a, "leetcode"))