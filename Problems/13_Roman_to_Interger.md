# 13 Roman to Interger 罗马数字转整数
## 题目描述
罗马数字转整数

## 解题思路

写一个字典存储对应关系，然后从头到尾扫描字符串，如果遇到特殊情况特殊处理。速度还可以，但是内存消耗大。

## 代码

```python3

class Solution:
    def romanToInt(self, s):
        a = {"I":1, "V":5, "X":10, "L":50, "C":100, "D":500, "M":1000}
        s = list(s)
        sum = 0
        for i, c in enumerate(s):
            sum += a[c]
            if i<len(s)-1:
                if c=="I" and (s[i+1]== "V" or s[i+1]=="X"):
                    sum -= 2
                if c=="X" and (s[i+1]== "L" or s[i+1]=="C"):
                    sum -= 20
                if c=="C" and (s[i+1]== "D" or s[i+1]=="M"):
                    sum -= 200                

        return sum

```