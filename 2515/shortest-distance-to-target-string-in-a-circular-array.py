# LeetCode 2515. Shortest Distance to Target String in a Circular Array
# 從 words 的 startIndex 出發，可往右走 or 往左走，希望走到 target 要幾步
class Solution:
    def closetTarget(self, words: List[str], target: str, startIndex: int) -> int:
        N = len(words)

        for i in range(N): # 由近到遠，逐一試各種距離
            if words[(startIndex+i)%N]==target: return i
            if words[(startIndex-i)]==target: return i

        return -1 # 找不到的話，就回傳 -1
