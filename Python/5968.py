#!/usr/bin/env python3
from typing import List
class Solution:
	def numberOfBeams(self, bank: List[str]) -> int:
		sum = 0
		temp = [0]* len(bank)
		for i in range(len(bank)):
			temp[i] = list(bank[i]).count('1')
		print(temp)
		j = 0
		for i in temp:
			if i==0:
				continue
			else:
				sum += i * j
				j = i
		return(sum)
a = Solution()
b = ["011001","000000","010100","001000"]
Solution.numberOfBeams(a, b)