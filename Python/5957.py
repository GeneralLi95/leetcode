#!/usr/bin/env python3
from typing import List
class Solution:
	def addSpaces(self, s: str, spaces: List[int]) -> str:
		result = ''
#		for i, char_s in enumerate(s):
#			if i in spaces:
#				result += " "
#				result += char_s
#			else:
#				result += char_s
		result = s[0:spaces[0]]
		for i in range(len(spaces)-1):
			result += " "
			result += s[spaces[i]:spaces[i+1]]
		result += " "	
		result += s[spaces[-1]:]
		return(result)
			
a = Solution()
b = "LeetcodeHelpsMeLearn"
c = [8,13,15]
Solution.addSpaces(a, b, c)