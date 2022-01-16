#!/usr/bin/env python3
# 格雷编码
# Medium  知识点 位运算 数学 回溯
# https://leetcode-cn.com/problems/gray-code/solution/gray-code-jing-xiang-fan-she-fa-by-jyd/ 这个解法实在是太妙了

from typing import List
class Solution:
	def grayCode(self, n: int) -> List[int]:
		res, head = [0], 1
		for i in range(n):
			for j in range(len(res)-1, -1, -1):
				res.append(head+res[j])
			head <<= 1
		return res
		
		
a = Solution()
b = 2
Solution.grayCode(a, b)