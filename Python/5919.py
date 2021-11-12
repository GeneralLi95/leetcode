#!/usr/bin/env python3

class Solution:
	def countVowels(self, word: str) -> int:
		sum = 0
		for i in range(len(word)):
			if(word[i] in ['a', 'e', 'i', 'o', 'u']):
				sum = sum + (len(word) - i)*(i+1)
		return(sum)
		
a = Solution()
print(Solution.countVowels(a, "noosabasboosa"))