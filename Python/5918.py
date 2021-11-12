#!/usr/bin/env python3

class Solution:
	def countVowelSubstrings(self, word: str) -> int:
		yuanyin = ['a','e','i','o','u']
		num = 0
		for i in range(len(word)-5):
			son = word[i:i+]
			print(son)
			if (set(son)== set(yuanyin)) :
				num+=1


#				print(son, flag)
		print(num)
##	
a = Solution()
Solution.countVowelSubstrings(a,"cuaieuouac")


