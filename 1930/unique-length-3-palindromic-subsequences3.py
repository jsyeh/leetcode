# LeetCode 1930. Unique Length-3 Palindromic Subsequences
# s 字串裡，可湊出「幾種」3個字母的迴文？ ex. aabca 會有 aaa, aba, aca 三種
# 26種字母，最多迴文才 (頭尾同)26*(中間)26 種。
# 記錄「最早出現的字母」start，中間的字
class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        table = defaultdict(set)  # 2個字母的表格，把「開頭」對應「中間的字」先放好
        start = set()  # 「開頭」候選人
        ans = set()  # 裡面會放「迴文」
        for c in s:
            # 先處理 cbc 3個字母的迴文：「開頭」c「中間」b「結尾」c
            for b in table[c]:  # 字首c、中間b
                ans.add(c+b+c)  # 現在讀到的字母c當結尾，把cbc迴文，加入答案
            # 再處理 ac 2個字母的表格
            for a in start:  # 針對曾經出現的每種「開頭」a字首候選人
                table[a].add(c)  # 把 c 當「未來」迴文的「中間」字母
            # 最後，將 c 加入「開頭」字首
            start.add(c)
        return len(ans)  # 目前累積的全部「迴文」
