# LeetCode 2011. Final Value of Variable After Performing Operations
# "++X", "X++", "--X", "X--" 共四種操作，X 開始是 0 問最後結束時 X 的值
class Solution:
    def finalValueAfterOperations(self, operations: List[str]) -> int:
        x = 0
        for op in operations:  # 針對每個指令操作
            if op[1]=='+': x += 1  # 有 + 號，就 +1
            else: x -= 1  # 沒 + 號，就 -1
        return x
