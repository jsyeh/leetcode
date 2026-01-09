# LeetCode 1207. Unique Number of Occurrences
# arr 陣列裡，是否每個數字「出現的次數」都不同
class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        freq = Counter(arr)  # 每個數的出現次數
        counter = Counter(freq.values())  # 想知道「出現次數」是否都不同
        for c in counter:  # 逐一檢查「出現次數」的統計量
            if counter[c] > 1: return False  # 有相同，就失敗
        return True
