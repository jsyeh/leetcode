# LeetCode 3227. Vowels Game in a String
# 兩人依序將字串 s 裡刪掉一些 substring
# 裡面 Alice 要刪「含奇數個母音」的substring、Bob 要刪「含偶數個母音」的substring
# 兩人都盡力玩，最後 Alice 會得勝嗎？
# 這題其實「字音」完全不重要。數一數「有幾個母音」即可
class Solution:
    def doesAliceWin(self, s: str) -> bool:
        vowelSet = set('aeiou')  # 可快速找「母音」
        N = 0  # 統計「母音的數量」
        for c in s:
            if c in vowelSet: N += 1  # 遇到「母音」+1
        if N > 0: return True  # 先手的 Alice 只要能取，就一定可以「得勝」
        else: return False
        '''  # 本來用下面「函式呼叫函式」試過全部可能。後來發現「Alice很容易得勝」
        # 有了「母音」的數量，接下來變成「減數字」的問題
        @cache  # 利用「函式呼叫函式」解這一題
        def helper(n, p):  # 母音數量n、奇偶性p(1奇 2偶)
            for i in range(p, n+1, 2):  # 每次可「取幾個」
                # 換「對手」玩、調整規則：數量變 n-i，p的1，2反過來
                if helper(n-i, 3-p) == False:  # 只要「對手」有任一種會輸
                    return True  # 那我就勝了！
            return False  # 都沒有得勝，就輸了QQ
        return helper(N, 1)
        '''
