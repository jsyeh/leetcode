class Solution:
    def getSmallestString(self, s: str) -> str:
        # 可以把2個parity相同的相鄰的數交換1次
        s = list(s)
        for i in range(len(s)-1):
            if int(s[i])%2 == int(s[i+1])%2 and int(s[i])>int(s[i+1]):
                temp = s[i]
                s[i] = s[i+1]
                s[i+1] = temp
                return ''.join(s)
        return ''.join(s)

