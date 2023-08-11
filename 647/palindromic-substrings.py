# 題目不只要找 Palindrome迴文substring，而且要算「總共有幾個」
class Solution:
    def countSubstrings(self, s: str) -> int:
        N = len(s)
        table = [[False]*N for _ in range(N)]
        # table[left][right] 表示有 left...right 是迴文（右包含）

        for i in range(N): # 長度為1的迴文，全部都是
            table[i][i] = True # 長度為1的單一字母，一定是迴文
        
        ans = N # 所以 ans 最少也有 N 個

        for i in range(N-1): # 再查 長度為2的疊字迴文
            if s[i] == s[i+1]:
                table[i][i+1] = True # 要記得標示迴文哦！
                ans +=1
        # print(ans)

        for length in range(3, N+1): # 長度從3到全長N: range(3,N+1)
            for left in range(0, N-length+1): # 左邊界 0...N-length
                right = left + length - 1 # 右包含
                # print(left, right, length)
                if s[left] == s[right] and table[left+1][right-1]==True:
                    table[left][right] = True #外相同，裡面迴文，太好了
                    ans += 1 # 又多一個迴文
        return ans
# case 42/130: "aaaaa"
