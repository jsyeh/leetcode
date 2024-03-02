# 26個字母，每個字母，有自己的寬度 widths[i]。一行字的寬度是 100 pixels
# 所以如果某個字母加入後「超過100」就要跳行。
# 給字串 s 及「字母對應的 widths」問「有幾行」及「最後一行有幾個pixels」
# 其實照著 s 字串，逐字母模擬即可。
class Solution:
    def numberOfLines(self, widths: List[int], s: str) -> List[int]:
        lineN = 1 # 目前有幾行字
        pixels = 0 # 最後一行，目前的寬度是多少 pixels
        for c in s: # 逐個字母處理
            if pixels + widths[ord(c)-ord('a')] > 100: # 寬度會超過100，就跳行
                lineN += 1 # 換新的一行
                pixels = widths[ord(c)-ord('a')] # 多放1個字
            else: # 塞得進 100 pixels 的話
                pixels += widths[ord(c)-ord('a')] # 就塞進去吧
        return [lineN, pixels] # 題目希望回傳2個值
