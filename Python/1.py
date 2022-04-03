class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        a = {}
        for i, num in enumerate(nums):
            if target - num in a:
                return [a[target - num], i]
            else:
                a[num] = i
        return none
    


sol = Solution()
l1 = [2, 7, 11, 15]
t = 9

print(sol.twoSum(l1, t))