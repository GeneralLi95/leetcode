class Solution:
	def searchRange(self, nums: [int], target: int) -> [int]:
		if len(nums) == 0:
			return [-1,-1]
		if len(nums) == 1:
			if nums[0] == target:
				l, r = 0, 0
			else:
				l, r = -1, -1
				
		def find_left(nums, target):
			left , right = 0, len(nums) - 1
			while left<right:
				mid = (left+right)//2
				if nums[mid] < target:
					left = mid + 1
				else:
					right = mid
			if nums[left]!= target:
				return -1
			return left
		
		
		
		def find_right(nums, target):
			left , right = 0, len(nums)
			while left<right:
				mid = (left+right)//2
				if nums[mid] > target:
					right = mid
				else:
					left = mid + 1
			if nums[right-1]!= target:
				return -1
			return (right - 1)
		
		l = find_left(nums, target)
		r = find_right(nums, target)
		
		
		return [l ,r ]
			
a = Solution()
b = [2, 2, 2]

print(Solution.searchRange(a, b, 2))