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