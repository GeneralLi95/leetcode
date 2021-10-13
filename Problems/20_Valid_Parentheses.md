# 20 Valid Parentheses 有效括号
## 题目描述
检查输入括号是否为有效括号

## 解题思路
典型的栈解法，根据数据特点加入了一些判断条件，希望能进行优化，但是这些判断似乎没有用上，高赞答案过于 Pythonic 不提倡。

第一个判断，是否左括号，左括号入栈，如果不是左括号，判断是否和栈顶括号配对，不配对False，配对输出。栈中始终只有左括号。
## 代码

```python3
class Solution:
    def isValid(self, s: str) -> bool:
        b = {'(':')',  '{': '}', '[':']'}
        a  = []
        for i in s:
            if i in b:
                a.append(i)
            elif len(a) == 0 or b[a[-1]] != i:
                return False
            elif b[a[-1]] == i:
                a.pop()
                
        if len(a) == 0:
            return True
        else:
            return False
```

## 其他代码


Pythonic

```python3
class Solution:
    def isValid(self, s):
        while '{}' in s or '()' in s or '[]' in s:
            s = s.replace('{}', '')
            s = s.replace('[]', '')
            s = s.replace('()', '')
        return s == ''
```