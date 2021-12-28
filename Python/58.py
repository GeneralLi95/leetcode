class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        a = s.rstrip().split(' ')
        if len(a) > 0:
            return len(a[-1])
        else:
            return 0 