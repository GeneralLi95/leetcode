#!/usr/bin/env python3
# 查找和最小的k对数字
# Meedium

from heapq import *
from typing import List,  Optional
from collections import defaultdict, deque
from itertools import product,combinations,permutations

class ListNode: 
	def __init__(self, val=0, next=None):
		self.val = val
		self.next = next

# -------------------------
class Solution:
	def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
		m, n = len(nums1), len(nums2)
		ans = []
		pq = [(nums1[i] + nums2[0], i ,0) for i in range(min(k, m))]   # 构建了一个堆
		print(pq)
		while pq and len(ans) < k:
			_, i, j = heappop(pq)   # 堆顶输出,保证输出的永远是最小值
			print(pq)
			ans.append([nums1[i], nums2[j]])
			if j + 1 < n:
				heappush(pq, (nums1[i] + nums2[j+1], i, j+1))  # 加入堆
				print("调整后的堆", pq)
		return ans
		
# -------------------------
		
a = Solution()
b = [1,1,2]
c = [1,2,3]

print(Solution.kSmallestPairs(a, b, c, 10))