# 想要把所有 Plaindrome 迴圈 都組合出來
# 先統計字母出現次數，再函式呼叫函式 來合成 DFS
class Solution:
    def generatePalindromes(self, s: str) -> List[str]:
        H = defaultdict(int) # 字母出現次數 Histogram統計
        # 統計完字母出現次數
        for c in s:
            H[c] += 1

        # 若無法湊成 Palindrome 就 False
        odd = 0
        for c in H:
            if H[c]%2==1: odd += 1
        if odd>1: return [] # 沒有答案

        # 利用 recursion 逐一減少字母、生成、再還原
        ans = []
        def helper(s1, s2, H, N):
            if N==0: ans.append(s1+s2)
            for c in H:
                if N>=2 and H[c]>=2: # 挑2個，前後放
                    H[c] -= 2 # 先拿走
                    helper(s1+c, c+s2, H, N-2)
                    H[c] += 2 # 再放回去
                if N==1 and H[c]==1: # 只剩1個放中間
                    ans.append(s1+c+s2)
        helper('', '', H, len(s))
        return ans
        
