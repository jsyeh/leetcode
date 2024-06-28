# 計算「沒有重覆字母」的substring有幾個
# 每個不同的i,j對應不同substring，但不能用2個迴圈O(n*n)（會超時）
# 所以可以用「毛毛蟲」法，只要O(n)的時間即可
class Solution:
    def numberOfSpecialSubstrings(self, s: str) -> int:
        H = defaultdict(int)  # 對應「字母」出現的次數（整數）
        ans = 0
        j = 0  # 對應左邊的尾巴
        for i, c in enumerate(s):  # i 對應右邊的頭，也就是「右界」
            H[c] += 1
            while H[c]>1: # 有重覆的話，尾巴要縮短才行
                H[s[j]] -= 1 # 尾巴吐出字母s[j]，要減1
                j += 1 # 真的縮短
            ans += i - j + 1 # 右界為i的這些substring全部上
            # （分別是j...i的各種縮短版，右界不動、左界可縮短）
        return ans
