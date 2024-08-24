# LeetCode 564. Find the Closest Palindrome
# 給個字串，找到「最接近」的「迴文」。今天全身疲憊，決定直接看 Solutions 裡最多人按讚的 GraceMeng 的解答分析：
# 12321 的 palindromeRoot 是左半 123，前一個是 122，後一個是123。答案就會是 12221、12321、12421 其中一個
# 12345 的 palindromeRoot 是左半123，前一個是 122，後一個是123。答案就會是 12221、12321、12421 其中一個
# 123456 的 palindromeRoot 是左半123，前一個是 122，後一個是123。答案就會是 122221、123321、124421 其中一個
# 另有3個奇怪的速解：(1) 1..9 可減1（個位數），10、100、1000等，也可減1（變一堆9）
# (2) 11,101,1001,10001 等，可以減2，變一堆9
# (3) 99,999,9999,99999 可以加2，變成前面的 101,1001,10001等
class Solution:
    def nearestPalindromic(self, n: str) -> str:
        if int(n)<=10: return str(int(n)-1) # 奇怪的速解1
        if n[0]=='1' and int(n[1:])==0: return str(int(n)-1) # 奇怪的速解1
        if n[0]=='1' and n[-1]=='1' and n.count('0')==len(n)-2: return str(int(n)-2) # 奇怪的速解2
        if len(n)==n.count('9'): return str(int(n)+2) # 奇怪的速解3
        # 接下來不能用速解法，改成「先找出 palindromeRoot」，再試 -1,0,+1 組出的字串「與n」的距離
        N = len(n) # 字串的長度
        if N%2==0: # 偶數，直接長度一半
            palindromeRoot = int(n[:(N//2)]) # 前半的整數
            ans0 = str(palindromeRoot-1) + str(palindromeRoot-1)[::-1]  # 前一個palinromeRoot 對應的迴文
            ans1 = str(palindromeRoot) + str(palindromeRoot)[::-1]  # palindromeRoot 本身對應的迴文
            ans2 = str(palindromeRoot+1) + str(palindromeRoot+1)[::-1]  # 後一個palinromeRoot 對應的迴文
        else: 
            palindromeRoot = int(n[:(N//2+1)]) # 前半的整數
            ans0 = str(palindromeRoot-1) + str(palindromeRoot-1)[::-1][1:]  # 前一個palinromeRoot 對應的迴文
            ans1 = str(palindromeRoot) + str(palindromeRoot)[::-1][1:]  # palindromeRoot 本身對應的迴文
            ans2 = str(palindromeRoot+1) + str(palindromeRoot+1)[::-1][1:]  # 後一個palinromeRoot 對應的迴文
        ans = [[abs(int(ans0)-int(n)), ans0], [abs(int(ans1)-int(n)), ans1], [abs(int(ans2)-int(n)), ans2]] # 三組迴文（要比距離）
        ans.sort() # 照著數字的「距離」排序
        if ans[0][1]==n: return ans[1][1]  # 若不幸n本身也是迴文，因不能挑自己本身，要換下一個最近的數
        else: return sorted(ans)[0][1]  # 直接距離最小迴文即可
        
