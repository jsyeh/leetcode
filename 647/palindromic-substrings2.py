# 想計算「總有有幾個palindrome迴文的substring」
# 之前用類似DP的作法，在table[i][j]標示i..j是否為迴文
# 今天又遇此挑戰題，想試另一種寫法。
# 我試試submissions裡隨挑個比我快的寫法，有人用 extend() 配while迴圈暴力試
class Solution:
    def countSubstrings(self, s: str) -> int:
        N = len(s)
        def extend(i,j)->int: # 找出 s[i] s[j] 分別「左右」展開的答案
            while i>=0 and j<N and s[i]==s[j]: # 只要有迴文，且可擴展
                i -= 1 # 往左擴展
                j += 1 # 往右擴展
            # 離開while時，一定不合理、多走1格。
            #maxLen = j - i - 1 # 便確認長度
            # 長度再折半，便是「有幾個 palindrome的個數」
            #if maxLen%2==0: return maxLen//2 # 偶數對折
            #else: return maxLen//2 + 1 # 奇數，要加1再對折
			return (j-i)//2 # 直接這樣寫，同時照顧了奇數與偶數
        
        ans = 0
        for i in range(N): # 逐個當中心來測試
            ans += extend(i,i) # 奇數對稱
            #if i<N-1: # 若右邊界可i+1
            #    ans += extend(i,i+1) # 偶數對稱
			ans += extend(i,i+1) # 不用加if也行，因extend()會檢查
        return ans
