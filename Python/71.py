#!/usr/bin/env python3
# 简化路径 字符串 栈
# Mediuem
# 最后怎么还有一个 '...' 情况 服了！ 
# 关键在于用 / 先 split 一下
from collections import *

#class Solution:
#	def simplifyPath(self, path: str) -> str:	
#		p = list(path)
#		d = deque(['',''])
#		r = deque([])
#		temp = 0
#		for i in p:
#			d.appendleft(i)
#
#			print('d',d, 'i',i)
#
#			if d[0] == '.' :
#				d.popleft()
#				temp += 1
#			else:
#				temp = 0
#			if d[0] == d[1] == '/':
#				d.popleft()
#
#			print('temp', temp)
#			if temp == 2 :
#				d.popleft()
#				while d[0] != '/' and len(d)!=2:
#					d.popleft()
#				temp = 0
#			if len(d) == 2:
#				d.appendleft('/')
#
#		if d[0] =="/":
#			d.popleft()
#
#			
#		d.pop()
#		d.pop()
#		if len(d) == 0:
#			return '/'
#		for i in d:
#			r.appendleft(i)
#		return ''.join(r)


class Solution:
	def simplifyPath(self, path: str) -> str:
		names = path.split("/")
		stack = list()
		for name in names:
			if name == "..":
				if stack:
					stack.pop()
			elif name and name != ".":
				stack.append(name)
		return "/" + "/".join(stack)
	
	
	
a = Solution()
b = "/home//foo/"
b2 = "/a/./b/../../c/"
b3= "/../"
b4 = "/a//b////c/d//././/.."
b5= "/a/../../b/../c//.//"
print(Solution.simplifyPath(a, b5))