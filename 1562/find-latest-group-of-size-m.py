# Input arr = [3,5,1,2,4] 表示 1...n=5，有5個bits去排列組合。00000 閞始，
# 3就變成 00100，再5就變成00101，再1就變成10101，再2就變成11101，再4就變成11111
# 可查到1有哪些 groups，題目的m是表示「最後機會」有m個1的那個group是在第幾步出現
# 所以 m=1 的話，在第 3,5,1,2 時，還有「最後機會」有單個 1 的 group，之後就沒機會了
class Solution:
    def findLatestStep(self, arr: List[int], m: int) -> int:
        ans, N = -1, len(arr)
        if N == m: return N # 要在最後一步，才會湊齊m個1

        length = [0]*(N+2) # 用來記錄「有幾個1」
        # length[a] 表示第a個bit是時，對應「連續幾個1」
        for i in range(N):
            a = arr[i]
            left, right = length[a-1], length[a+1]
            # 在最邊綠的地方（也就是 0-1交界的那個1）存「這個集團有幾個連續的1」
            length[a-left] = length[a+right] = left + right + 1
            # 左邊緣、右邊綠，都可查到這個集團對應 left+right+1 個1
            if left==m or right==m: # 舊的集團結束前，剛好長度m的話，記下來「第幾步發生」
                ans = i
        return ans # 所以最後一次發生的時機，就會記在 ans 裡

