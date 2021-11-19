#!/usr/bin/env python3
class Solution:
	def search(self, nums: [int], target: int) -> int:
		def search2(nums:[], i, j, target):
			left = i
			right = j-1
			print(i, j)
			while left <= right:
				mid = (left+right)//2
				# print('mid=',nums[mid])
				if nums[mid] == target:
					return mid
				elif nums[mid] > target:
					right = mid - 1
				else:
					left = mid + 1
					
		point = nums.index(max(nums))
		print(point)
		if target == nums[point]:
			return point
		# if point==0 or point==len(nums):
		#     return -1
		
		if  search2(nums, 0, point+1, target)==None and search2(nums, point+1,len(nums),target)==None:
			return -1
		if search2(nums, 0, point+1, target) != None:
			return search2(nums, 0, point+1, target)
		else:
			return search2(nums, point+1, len(nums),target)
		
a = Solution()
print(Solution.search(a, [4,5,6,7,0,1,2], 0))