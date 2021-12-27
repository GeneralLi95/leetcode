#!/usr/bin/env python3
from typing import List
class Solution:
	def kIncreasing(self, arr: List[int], k: int) -> int:
#		sum = 0
#		print(arr)
#		print(len(arr))
#		for i in range(len(arr) - k):
#			if arr[i] > arr[i+k]:
#				arr[i+k] = arr[i]
#				sum += 1
#		print(arr)
#		print(sum)
		dp = [1] * len(arr)
		for i in range(len(arr)):
			for j in range(0, i, k ):
				if arr[j] <= arr[i]:
					dp[i] = max(dp[i], dp[j] + 1)
		print(dp)
		print (len(arr)//k - max(dp))
		
		
		
a = Solution()
b = [4,1,5,2,6,2]
c = 3
b2 = [5,4,3,2,1]
c2 = 2

b3 = [12,6,12,6,14,2,13,17,3,8,11,7,4,11,18,8,8,3]
c3 = 1
Solution.kIncreasing(a, b, c)