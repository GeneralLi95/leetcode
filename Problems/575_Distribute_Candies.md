# 575 Distribute Candies 分糖果
## 题目描述

给定一个偶数长度的数组，其中不同的数字代表着不同种类的糖果，每一个数字代表一个糖果。你需要把这些糖果平均分给一个弟弟和一个妹妹。返回妹妹可以获得的最大糖果的种类数。

## 解题思路

其实是 无重复元素数目 和 半数之间的最小值。

题目思路非常清晰，找出无重复的所有糖果数目，如果这个数字小于一半，那么答案就是这个数字，如果这个数字大于一半，因为每个小孩最多只能拿一半糖果，所以结果就是一半。

这个问题的关键就是如何找出无重复的所有糖果数目，结果Python有一个自己数据结构，集合set，直接链表转集合再转链表，求一下长度就是无重复的所有糖果数目了。

## 代码
```python3
class Solution:
    def distributeCandies(self, candies: List[int]) -> int:
        mid = len(candies)//2
        min_candy = len(set(candies))

        return min(mid, min_candy)
```