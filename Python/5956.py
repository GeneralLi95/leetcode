#!/usr/bin/env python3
from typing import List
class Solution:
	def firstPalindrome(self, words: List[str]) -> str:
		for i in words:
			if i[::-1] == i:
				return(i)
		return ("")
			
a = Solution()
b = ["abc","car","ada","racecar","cool"]
print(Solution.firstPalindrome(a, b))