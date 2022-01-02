#!/usr/bin/env python3

# 消除游戏 最后执行的输入：1000000

# -------模拟法，暴力解法，无法通过最后一个测试点
#def delete_item(temp):
#	res = [None] * (len(temp)//2)
#	for i in range(len(res)):
#		res[i] = temp[2*i+1]
#	return res
#
#class Solution:
#	def lastRemaining(self, n: int) -> int:
#		result = [i for i in range(1,n+1)]
##		print(result)
##		print(delete_item(result))
#		while True:
#			if len(result) == 1:
#				return result[0]
#			
#			result = delete_item(result)
#			result = result[::-1]
#——————————————————————————————————————————————

class Solution:
	def lastRemaining(self, n: int) -> int:
		a1 = 1
		k, cnt, step = 0, n, 1
		while cnt > 1:
			if k % 2 == 0:  # 正向
				a1 += step  # 正向 第一个数一定被删除
			else:
				if cnt % 2:      # 反向需要判断，如果是奇数项，第一个数被删除，如果是偶数，第一项不被删除
					a1 += step   
			k += 1
			step *= 2
			cnt //= 2
		return a1
			
a = Solution()
b = 1000000
print(Solution.lastRemaining(a, b))