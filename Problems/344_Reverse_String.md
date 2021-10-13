# 344 Reverse String
## 题目描述

其实就是输入一个链表，输出反链表。

## 解题思路

Python 的链表自带 [::-1]其实可以直接转，但是过于 Pythonic，所以还是实现了一个双指针，从两边到中间的方法，只不过Python没有指针罢了。Python换位比较方便，不需要引入中间变量。


## 代码

```python3
class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        for i in range(len(s)//2):
            (s[i], s[-(i+1)])= (s[-(i+1)], s[i])
```

