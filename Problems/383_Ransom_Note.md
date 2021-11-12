# 383 Ransom Note 赎金信
## 题目描述
两个字符串，赎金信ransom和杂志magazine，判断 `ransom` 能否由 `magazines` 里面的字符构成，如果可以返回`true`，如果不行返回`false`。注意`magazine`中的每个字符只能用一次。

## 解题思路
这个题英文翻译成中文叫赎金信，很有赎回的味道，一个magazines里面的字符可以赎回一个ransom里面的字符。所以就遍历ransom字符串，每遍历一个在magazine字符串里面删除一个，如果能够遍历完成，返回true，否则返回false。那么中间异常情况最好的处理办法就是Python中的 try except语句。

## 代码

```python
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        a = list(ransomNote)
        b = list(magazine)

        try:
            for i in a:
                b.remove(i)
            return True
        except:
            return False
```

