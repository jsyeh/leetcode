# LeetCode 1358. Number of Substrings Containing All Three Characters
# s 字串裡，有幾個 substring 裡，有湊齊 a,b,c 三種字母。
class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        # 看到有個特別的寫法「記錄每個字母」最後出現的位置
        last = {'a':-1, 'b':-1, 'c':-1}  # -1 代表「還沒出現過」
        count = 0
        for i, c in enumerate(s):
            last[c] = i  # 現在字母「對應的位置」
            good = min(last.values())  # 對應「之前三種字母湊齊」的位置
            count += good + 1  # good 到 i 之間，含有「三種字母」
            # 那 0...good 都能是 substring 字串開頭，i是 substring 結尾，有good+1種可能
            # 若有字母還沒出現過，good 會是 -1 。 -1＋1 會是 0 還無法「累積答案」
        return count
