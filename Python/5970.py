#!/usr/bin/env python3
from typing import List
from collections import *
import operator
class Solution:
	def maximumInvitations(self, g: List[int]) -> int:
		n = len(g)		
		rg = [[] for _ in range(n)]   # 图 g 的反图
		deg = [0] * n    # 图 g 上每个节点的入度
		
		for v, w in enumerate(g):
			rg[w].append(v)
			deg[w] += 1
		
		print('g',g)
		print('rg',rg)
		print('deg', deg)
		
		# 拓扑排序 剪掉图 g 上 的所有树枝
		q = deque(i for i,d in enumerate(deg) if d == 0)
		print('q', q)
		while q:
			v = q.popleft()
			w = g[v]
			deg[w] -= 1
			if deg[w] == 0:
				q.append(w)
		print('q', q)
		print('deg', deg)
		
		# 通过反图 rg 寻找 树枝上最深的链
		def rdfs(v: int) -> int:
			max_depth = 1  
			for w in rg[v]:
				if deg[w] == 0:   # 树枝上的点 在经拓扑排序后，入度均为 0
					max_depth = max(max_depth, rdfs(w) + 1)
			return max_depth
#		
#		
		max_ring_size, sum_chain_size = 0, 0
		for i, d in enumerate(deg):
			if d <= 0:
				continue 
			# 遍历基环上的点 （拓扑排序后入度大于0）
			deg[i] = -1
			ring_size = 1
			v = g[i]   # 去原图 找下一个节点 
			while v != i:
				deg[v] = -1
				ring_size += 1
				v = g[v]
			print(ring_size)
			if ring_size == 2: # 基环大小为2
				sum_chain_size += rdfs(i) + rdfs(g[i])
			else:
				max_ring_size = max(max_ring_size, ring_size)
#		
		return max(max_ring_size, sum_chain_size)
					
					
		
#		print('g',g)
#		print('rg',rg)
#		print('deg', deg)
#					
#		num_idx = defaultdict(list)
#		graph = []
#		for i, idx in enumerate(favorite):
#			num_idx[idx].append(i)
#
#		print(num_idx)
			
		
a = Solution()
b = [2,2,1,2]
b2 = [3,0,1,4,1]
b3 = [1,0,0,2,1,4,7,8,9,6,7,10,8]  # 6
b4 = [21,12,1,7,5,6,20,2,14,15,12,14,2,20,0,17,23,12,17,13,11,13,3,11]
print(Solution.maximumInvitations(a, b4))