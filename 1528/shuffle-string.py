# 要把字串的字母，利用 indices[i] 放到對應的位置
class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        N = len(s)
        ans = [0]*N
        for i in range(N):
            ans[indices[i]] = s[i] # 照對照表，將字母放到對應位置
        return ''.join(ans) # 再把字母join()接起來
