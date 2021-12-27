# 1 Two Sum 两数之和
## 题目描述

给定一个整数数组 `nums` 和一个目标值 `target`，请你在该数组中找出和为目标值的那 两个 整数，并返回他们的数组下标。

你可以假设每种输入只会对应一个答案。但是，数组中同一个元素不能使用两遍。

## 解题思路

哈希表，做一个结果列表，记录下位置，然后符合结果立刻对应过去。Python 哈希表 `enumerate`

## 代码
Python 的哈希表是Enumerate
```python
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        a = {}
        for i, num in enumerate(nums):
            if target - num in a:
                return [a[target - num], i]
            else:
                a[num] = i
        return none
```
Java的哈希表是 Map或者HashMap

```Java

class Solution {
    public int[] twoSum(int[] nums, int target) {
        Map<Integer, Integer> map = new HashMap<>();
        for(int i = 0; i< nums.length; i++) {
            if(map.containsKey(target - nums[i])) {
                return new int[] {map.get(target-nums[i]),i};
            }
            map.put(nums[i], i);
        }
        throw new IllegalArgumentException("No two sum solution");
    }
}
```

