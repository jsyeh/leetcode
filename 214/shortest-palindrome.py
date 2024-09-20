# LeetCode 214. Shortest Palindrome
# 在字串 s 前面加字母，可變成 palindrome迴文，找到「最短迴文」
# ex. "aabaaa" 可變成 "aaabaaa" 或 "aaabaabaa" 要找最短的
# 很難的原因，是「字長很長 5*10^4」不能暴力迴圈去試。
# 有張示意圖，[非迴文倒過來] [重疊迴文] [非迴文] 就寫了本版本，沒想到「最後一筆測資」用盡memory嗚嗚
# Editorial 的 Approach 4 介紹 Rolling Hash Based 演算法，用「自製 Hash 函式」可結省大量memory
class Solution:
    def shortestPalindrome(self, s: str) -> str:
        # prefix_reverse = set()  # prefix字串「倒過來」的版本，將全部記起來
        r = s[::-1]  # 事先準備 reversed「倒過來」的字串，方便製作 prefix_reverse 可節省時間
        prefix_palindrome = 1  # 「字首prefix」是迴文的長度，最短是只有最前面1個字母
        hash1, hash2 = 0, 0  # 自製 Hash 函式 Rolling Hash 方法，左邊hash1放正的、右邊hash2放倒過來的
        power_value = 1  # 自製 Hash 函式 Rolling Hash 用來乘的數，越乘越大
        MOD = 10**9 + 7  # 自製 Hash 函式 時，取餘數的超大質數
        for i in range(len(s)):  # 要處理 prefix字串 s[:i+1]
            hash1 = (hash1 * 29 + ord(s[i])-96) % MOD  # 左往右加 正的新增1個字母，使用自製 Hash 函式
            hash2 = (hash2 + (ord(s[i]) - 96) * power_value) % MOD  # 倒過來新增1個字母，使用自製 Hash 函式
            power_value = (power_value * 29) % MOD  # 更新要乘的數，供 自製 Hash 函式使用
            if hash1 == hash2: prefix_palindrome = i + 1 # 自製有出現過，太好了，字首「迴文」長度變長了
            # prefix.add(s[:i+1])  # 把前面[:i+1]加入 hash set（後來發現不用這個）
            # prefix_reverse.add(r[-i-1:])  # 倒過來的後面（即前面[:i+1]反過來）加入 hash set
            # if s[:i+1] in prefix_reverse:  # 順手檢查「現在有沒有出現過」
            #     prefix_palindrome = i + 1  # 有出現過，太好了，字首「迴文」長度變長了
        adding = len(s) - prefix_palindrome  # 總長度 -「重疊」迴文長度，剩下要「補齊」長度
        return r[:adding] + s  # 將「非迴文倒過來」再接上原本的 s（內含[重覆迴文] [非迴文]) 就是答案
