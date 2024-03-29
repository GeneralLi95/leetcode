#!/usr/bin/env python3

# 801 使 序列递增的最小交换次数
# 动态规划

from typing import List
class Solution:
	def minSwap(self, A: List[int], B: List[int]) -> int:
		n1, s1 = 0, 1   # n1  前一状态 不交换  s1 前一状态 交换
		for i in range(1,len(A)):
			n2 = s2 = float("inf")  # 正无穷
			if A[i-1] < A[i] and B[i-1] < B[i]:
				n2 = min(n2, n1)         
				s2 = min(s2, s1 + 1)   # 交换了 就加1
			if A[i-1] < B[i] and B[i-1] < A[i]:
				n2 = min(n2, s1)
				s2 = min(s2, n1+1)
				
			n1, s1 = n2, s2
			print("i=",i,"   ",n1,s1)
			
		return min(n1,s1)
			
				
		
s = Solution()
a = [1,3,5,4]
b = [1,2,3,7]
print(Solution.minSwap(s, a, b))