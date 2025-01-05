# LeetCode 2381. Shifting Letters II
# 給你字串 s，接下來「把某段」往上撥0 or 往下撥1，問最後的字串是什麼
class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        # 只記錄 開始、結尾的位移量
        sh = [0] * (len(s)+1)  # 「起始、結束位移量」
        for start, end, d in shifts:
            if d==0: d = -1  # 0 代表往上撥，所以等下加 -1
            sh[start] += d  # 從 start 開始，會撥動
            sh[end+1] -= d  # 影響到 end 為止，所以 end+1 要「撥回去」
        s = list(s)  # Python 字串不能給值，所以改成 list
        d2 = 0  # 從左到右的「累積撥動」量
        def change2(c, d):  # 用函式，找到字母 c 撥動 d 位移後的結果
            # 把字母變 ascii 值，再變26字母範圍，加上位移量d，取26餘數。可能有負數，再加26 再取餘數，最後變回字母
            return chr(((ord(c)-ord('a')+d)%26 + 26) %26 + ord('a'))
        for i, c in enumerate(s):  # 針對每個字母
            d2 += sh[i]  # 依照「起始、結束位移量」，調整
            s[i] = change2(s[i], d2)  # 算出新的字母
        return ''.join(s)  # 把 list 變回字串

        # 笨方法，使用2層迴圈，一定會超過時間。只是給大家參考。不會真的執行
        s = list(s)
        def change(c, d):
            if d==0: return chr((ord(c)-ord('a')+25)%26 + ord('a'))
            else: return chr((ord(c)-ord('a')+1)%26 + ord('a'))
        for start, end, d in shifts:
            for i in range(start, end+1):
                s[i] = change(s[i], d)
        return ''.join(s)
