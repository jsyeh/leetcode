# LeetCode 1207. Unique Number of Occurrences
# arr 陣列裡，是否每個數字「出現的次數」都不同
class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        counter = Counter(arr)  # 統計每個數的出現次數
        freq = set()  # 出現的次數，有哪些
        for c in counter:
            if counter[c] in freq: return False  # 「次數」出現過，就失敗
            freq.add(counter[c])
        return True
