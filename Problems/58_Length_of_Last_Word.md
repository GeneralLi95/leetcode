# 58 Length of Last Word 最后一个单词长度
# 题目描述
一个字符串只包含空格和大小写字母，给出其中最后一个单词的长度

如"hello world"给出5，"hello world    "得出也是5
# 解题思路
从右往左遍历找到第一个不是空格的单词输出长度

# 代码
class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        a = s.rstrip().split(' ')
        if len(a) > 0:
            return len(a[-1])
        else:
            return 0 

# 代码点评
用rstrip去掉空格和split切分稍显pythonic。
