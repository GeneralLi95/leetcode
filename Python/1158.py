#!/usr/bin/env python3

# 一周中的第几天
# 吉姆拉尔森计算公式
# https://baike.baidu.com/item/蔡勒公式/10491767

class Solution:
	def dayOfTheWeek(self, day: int, month: int, year: int) -> str:
		if month == 1:
			month = 13
			year -= 1
		if month == 2:
			month = 14
			year -= 1
		w = day + 2 * month + 3*(month+1) // 5 + year + year //4 - year //100 + year//400
		result = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday","Sunday"]
		res =  result [w % 7]
		return(res)
		
a = Solution()
print(Solution.dayOfTheWeek(a, 15, 8, 1993))