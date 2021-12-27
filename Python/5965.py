#!/usr/bin/env python3
from typing import List

from collections import defaultdict
#class Solution:
#	def getDistances(self, arr: List[int]) -> List[int]:
#		d = defaultdict(list)
#		for i,j in enumerate(arr):
#			d[j].append(i)
#		print(d)
#		result = []
#		for i,j in enumerate(arr):
#			temp = sum(abs(q-i) for q in d[j])
#			print(i, j, "dj:", d[j], temp)
#			result.append(temp)
#		return result
# 我的做法，哈希表加双重循环 超时




class Solution:
	def getDistances(self, arr: List[int]) -> List[int]:
		n = len(arr)
		num_idxs = defaultdict(list)
		# 初始化哈希表
		for i, x in enumerate(arr):
			num_idxs[x].append(i)
		
		
		# 初始化结果数组
		res = [0 for _ in range(n)]
		
		#
		for x, idxs in num_idxs.items(): # 哈希表的循环调用值得学习
			print(x, idxs)
			idxn = len(idxs)
			
			l_sum = 0
			l_cnt = 0
			r_sum = sum(idxs)
			r_cnt = idxn

			for i in idxs:
				cur = (i * l_cnt - l_sum) + (r_sum - i * r_cnt)
				print(i, cur)
				res[i] = cur
				l_sum += i  # 前方和+i
				l_cnt += 1  # 前方数字+1
				r_sum -= i  # 后方和 -i
				r_cnt -= 1  # 后方数字 -1
		return res
a = Solution()
b = [2,1,3,1,2,3,3]
print(Solution.getDistances(a, b))