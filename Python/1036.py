#!/usr/bin/env python3
# 1036 逃出大迷宫
# Hard
# 深度优先搜索，广度优先搜索，数组，哈希表


from typing import List,  Optional
from collections import defaultdict, deque
from itertools import product,combinations,permutations

class ListNode: 
	def __init__(self, val=0, next=None):
		self.val = val
		self.next = next

# -------------------------

EDGE, MAX, BASE, DIR = int(1e6), int(1e5), 131, [(1, 0), (-1, 0), (0, 1), (0, -1)]
class Solution:
	def isEscapePossible(self, blocked: List[List[int]], source: List[int], target: List[int]) -> bool:
		block = {p[0] * BASE + p[1] for p in blocked}
		n = len(blocked)
		MAX = n * (n-1)//2 # 可直接使用 1e5
		def check(a, b):
			vis = {a[0] * BASE + a[1]}
			d = deque([a])
			while len(d) and len(vis) <= MAX:
				x, y = d.popleft()
				if x == b[0] and y == b[1]:
					return True
				for dx, dy in DIR:
					nx, ny = x + dx, y + dy
					if nx < 0 or nx >= EDGE or ny < 0 or ny >= EDGE:
						continue
					h = nx * BASE + ny
					if h in block or h in vis:
						continue
					d.append((nx, ny))
					vis.add(h)
			return len(vis) > MAX
		return check(source, target) and check(target, source)
	
		
# -------------------------
		
a = Solution()