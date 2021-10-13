# 1047 Remove All Adjacent Duplicates In String 删除所有相邻重复项

## 题目描述
删除所有相邻重复项直到无法删除为止

## 解题思路
典型的字符串应用，主要涉及出栈入栈操作，和第20题，括号配对非常相似。

## 代码

```python
class Solution:
    def removeDuplicates(self, S: str) -> str:
        a = []
        for i in S:
            if len(a) == 0:
                a.append(i)
            elif a[-1] == i:
                a.pop()
            else:
                a.append(i)
        return ''.join(str(i) for i in a)
```