# LeetCode 3208. Alternating Groups II
# colors 有一堆0和1，繞成圈。請問有幾種「長度為k」的片段，是0、1交錯？
class Solution:
    def numberOfAlternatingGroups(self, colors: List[int], k: int) -> int:
        # 善用 Python index 能「負」，把「後k-1項」檢測，找到壞掉位置，方便「繞圈圈」
        start = -k  # 好的「開始」標示在「負」的盡頭，若 i - start >= k 就湊足k個以上
        for i in range(-k+1, 0): # 先把「後k-1項」都檢查一次
            if colors[i-1]==colors[i]: start = i  # 若與前項「相同」，i 是「新的開始」
        
        ans = 0  # 現在開始，檢測「每一格」的前面，是否已湊齊「足夠多」的「交錯」
        for i in range(len(colors)):
            if colors[i-1]==colors[i]: start = i  # 若與前項「相同」，i 是「新的開始」
            if i - start >= k - 1:  # 頭尾相距 k-1 就代表「湊到k項」
                ans += 1  # 「前面」已湊齊「足夠多」項，就找到1筆答案
        return ans
