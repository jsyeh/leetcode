# LeetCode 1893. Check if All the Integers in a Range Are Covered
# 測試 left...right 裡的整數，是否都有在 ranges 裡
class Solution:
    def isCovered(self, ranges: List[List[int]], left: int, right: int) -> bool:
        s = set()
        for start,end in ranges:
            for now in range(start, end+1):
                s.add(now)
        for now in range(left, right+1):
            if now not in s: return False
        return True
