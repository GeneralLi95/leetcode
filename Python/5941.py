#!/usr/bin/env python3
from typing import List
from collections import defaultdict, deque

# 周赛时写的wrong anwser 没有考虑相同时间开会的应该统一处理

#class Solution:
#	def findAllPeople(self, n: int, meetings: List[List[int]], firstPerson: int) -> List[int]:
#		def takeSecond(elem):
#			return elem[2]
#		meetings.sort(key =takeSecond )
#		print(meetings)
#		result = [0, firstPerson]
#		
#		for meet in meetings:
#			
#			if meet[0] in result:
#				result.append(meet[1])
#			elif meet[1] in result:
#				result.append(meet[0])
#
#		return(list(set(result)))

	
# 官方题解
class Solution:
	def findAllPeople(self, n: int, meetings: List[List[int]], firstPerson: int) -> List[int]:
		m = len(meetings)
		meetings.sort(key = lambda x:x[2])
#		print(meetings)
		
		secret = [False] * n
		secret[0] = secret[firstPerson] = True
		
		i = 0
		while i < m:
			# meetings[i..j] 是同一时间
			j = i
			while j + 1 < m and meetings[j+1][2] == meetings[i][2]:   # 时间相同条件
				j += 1
			# 找到了 j
			
			vertices = set()  # 节点
			edges = defaultdict(list)
			for k in range(i, j+1):
				x , y = meetings[k][0], meetings[k][1]
				vertices.update([x, y])     # set.update 合并集合
#				print(vertices)
				edges[x].append(y)
				edges[y].append(x)
#				print("edges", edges)
				
			q = deque([u for u in vertices if secret[u]])
			while q:
				u = q.popleft()
				
				for v in edges[u]:
					if not secret[v]:
						secret[v] = True
						q.append(v)
			i = j + 1
		
		ans = [i for i in range(n) if secret[i]]
		return ans
		
a = Solution()
b = 6
c = [[3,4,2],[1,2,1],[2,3,1]]
c2 = [[0,2,1],[1,3,1],[4,5,1]]
d = 1
print(Solution.findAllPeople(a, b, c, d))