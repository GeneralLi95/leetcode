#!/usr/bin/env python3

class Solution:
	def timeRequiredToBuy(self, tickets: [], k: int) -> int:
		sum = 0
		while tickets[k]!=0:
			for i in range(len(tickets)):
				if tickets[i]!=0:
					sum+=1
					tickets[i] -=1
				if tickets[k] == 0:
					return sum

	
a = Solution()
print(Solution.timeRequiredToBuy(a, [2,3,2], 2))
print(Solution.timeRequiredToBuy(a, [5,1,1,1], 0))