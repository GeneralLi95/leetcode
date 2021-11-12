#!/usr/bin/env python3
class Solution:
	def generate(self, numRows: int) :
		def fac(n) -> int :
			result = 1
			if(n==0):
				return result
			else:
				for i in range(1,n+1):
					result *= i
				return result
			
		end = [] 
		for i in range(numRows):
			temp = []
			if(i==0):
				end.append([1])
			elif(i==1):
				end.append([1,1])
			else:
				for j in range(i+1):
					temp.append(fac(i)//(fac(j)*fac(i-j)))
				end.append(temp)
		return end
a = Solution()
print(Solution.generate(a, 5))
