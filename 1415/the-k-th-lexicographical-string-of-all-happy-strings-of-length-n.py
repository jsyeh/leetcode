# LeetCode 1415. The k-th Lexicographical String of All Happy Strings of Length n
# 只要「相鄰的字母不同」就是 happy string。從小到大，找第 k 個happy string
class Solution:
    def getHappyString(self, n: int, k: int) -> str:
        ans = []
        self.k = k  # 因為「函式」裡，會「動到k」所以用 self.k 才能用到同一個 k
        def dfs(i):  # 「函式呼叫函式」，嘗試修改第i個位數
            if i==n:  # 字串長度「湊到n個」，可「認真做判斷」
                # print(ans, self.k)  # 印出「長度為n」的happy string 並倒數
                self.k -= 1  # 耗掉 1 個 string，因為現在湊成 1 個 happy string
                if self.k==0: return True  # 當 k 耗盡時，就是找到第 k 個
                return False  # 沒有耗盡，就回傳（總之，長度夠，就不需再用下面的 for 迴圈）
            for now in "abc":  # 利用 for 迴圈，逐字母 'a' 'b' 'c'，慢慢測
                if i==0 or ans[i-1] != now:  # 可用「這個字母」（第0個字母 or 與前項不同）
                    ans.append(now)  # 塞到後面
                    if dfs(i+1):  # 「函式呼叫函式」，再繼續「深入測試」
                        return True  # 如果耗盡 k 就提早結束
                    ans.pop()  # 還原
        dfs(0)  # 「函式呼叫函式」，從0開始測
        return ''.join(ans)

