# 每次輸入字母 i 時，會把前面「全部反轉」
class Solution:
    def finalString(self, s: str) -> str:
        ans = []
        N = len(s)
        for i in range(N):
            if s[i]=='i':
                ans.reverse()
            else:
                ans.append(s[i])
        return ''.join(ans)
