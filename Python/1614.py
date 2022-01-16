#!/usr/bin/env python3

# 1614 括号的最大嵌套深度 

class Solution:
	def maxDepth(self, s: str) -> int:
		s = list(s)
		d1 = ['[','(','{']
		d2 = ['',')','}']
		result = []
		res = 0
		for i in s:
			if i in d1:
				result.append(i)
				res = max(res, len(result))
			if i in d2:
				result.pop()
		return res
				
			
		
a = Solution()
b = "(1+(2*3)+((8)/4))+1"
print(Solution.maxDepth(a, b))