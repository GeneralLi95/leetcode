class Solution:
    def lengthOfLongestSubstring(self, s):
        a = []
        result = 0
        for c in s:
            if c in a:
                length = len(a)
                result = max(length, result)
                i = a.index(c)
                a.append(c)
                a = a[i+1:]
                
            else:
                a.append(c)
                length = len(a)
                result = max(length, result)

        return result
