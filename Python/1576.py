#!/usr/bin/env python3

# 1576 替换所有的问号

class Solution:
	def modifyString(self, s: str) -> str:
		s = list(s)
		for i in range(len(s)):
			if s[i] == "?" and s[i-1] == "?":
				
				s[i] = "a"
				
			elif s[i] == "?":
				asc = ord(s[i-1]) + 1

				next = i+1
				if asc == 123:
					asc = 97
				if next == len(s):
					next = 0
				if asc == ord(s[next]):
					asc += 1
				if asc == 123:
					asc = 97


				
				s[i] = chr(asc)
				
		result = ''.join(s)

#	 官方题解，也很巧妙
#class Solution:
#	def modifyString(self, s: str) -> str:
#		res = list(s)
#		n = len(res)
#		for i in range(n):
#			if res[i] == '?':
#				for b in "abc":
#					if not (i > 0 and res[i - 1] == b or i < n - 1 and res[i + 1] == b):
#						res[i] = b
#						break
				
		return result
		
a = Solution()
b = "y?z"
print(Solution.modifyString(a, b))