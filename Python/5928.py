#!/usr/bin/env python3

class Solution:
	def decodeCiphertext(self, encodedText: str, rows: int) -> str:
		col = len(encodedText) // rows

		aaa = list(encodedText)
#		cube = [['*' for j in range(col)] for i in range(rows)] 
#		for i in range(rows):
#			for j in range(col):
#				cube[i][j] = aaa.pop(0)

		result = ''
		
		for j in range(col):
			for i in range(rows):
				if (i+j)<col:
					result += aaa[i* col +i +j ]
#					result += cube[i][i+j]
		return(result.rstrip())

		
a = Solution()
print(Solution.decodeCiphertext(a, "ch   ie   pr", 3))