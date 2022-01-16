#!/usr/bin/env python3

# 猫和老鼠
# Hard

from typing import List

DRAW = 0
MOUSE_WIN = 1
CAT_WIN = 2

class Solution:
	def catMouseGame(self, graph: List[List[int]]) -> int:
		n = len(graph)  # 节点数目
		dp = [ [ [-1] * (n * 2) for _ in range(n)] for _ in range(n)]
#		print(dp)
		
		def getResult(mouse: int, cat:int, turns: int) -> int:
			if turns == n * 2:
				return DRAW
			res = dp[mouse][cat][turns]
			if res != -1:
				return res
			if mouse == 0:
				res = MOUSE_WIN
			elif cat == mouse:
				res = CAT_WIN
			else:
				res = getNextResult(mouse, cat, turns)
			dp[mouse][cat][turns] = res
			return res

		def getNextResult(mouse:int, cat:int, turns:int) -> int:
			curMove = mouse if turns % 2 == 0 else cat   # 老鼠先动 然后 猫动
			defaultRes = MOUSE_WIN if curMove != mouse else CAT_WIN
			res = defaultRes
			for next in graph[curMove]:
				if curMove == cat and next == 0:
					continue    # 猫不能进洞 
				nextMouse = next if curMove == mouse else mouse  # 轮到老鼠动 则老鼠动，否则不动
				nextCat = next if curMove == cat else cat
				nextRes = getResult(nextMouse, nextCat, turns + 1)
				if nextRes != defaultRes:
					res = nextRes
					if res != DRAW:
						break
			return res
		
		
		return getResult(1, 2, 0) 
			
a = Solution()
b = [[2,5],[3],[0,4,5],[1,4,5],[2,3],[0,2,3]]
Solution.catMouseGame(a, b)