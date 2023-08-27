class Solution:
    def longestPalindrome(self, s: str) -> int:
        # 先統計所有字母出現的次數
        stat = {}
        for c in s:
            if c not in stat:
                stat[c] = 1
            else:
                stat[c] += 1
        
        ans = 0
        single = False
        for c in stat:
            ans += stat[c] //2 * 2 # 成雙有多少字母：先整數除法，再2倍，
            if stat[c]%2==1:
                single = True
        if single:
            ans += 1
        return ans
