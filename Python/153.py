class Solution:
    def findMin(self, nums: [int]) -> int:
        left = 0
        right = len(nums)
        while left < right:
            mid = (left + right)//2
            if nums[mid] <= nums[left]:
                right = mid
            else:
                left = mid
        if(left == len(nums) -1):
            left = -1
        return(nums[left+1])


b = [4,5,6,7,0,1,2]
b2 = [11,13,15,17]
    
a = Solution()
print(Solution.findMin(a, b2))