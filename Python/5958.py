#!/usr/bin/env python3
from typing import List

def cr(n):
	return n*(n-1)//2

class Solution:
	def getDescentPeriods(self, prices: List[int]) -> int:
		temp = 1
		sum = len(prices)
		for i in range(len(prices)-1):
			if (prices[i] - prices[i+1] == 1):
				temp += 1
			else:
#				print(temp)
				sum += cr(temp)
				temp = 1
		sum += cr(temp)
		return(sum)
				
		
a = Solution()
b = [4,3,2,1,4,3,2]
Solution.getDescentPeriods(a, b)