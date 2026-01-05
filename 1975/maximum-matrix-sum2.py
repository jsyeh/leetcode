# LeetCode 1975. Maximum Matrix Sum
# Matrix 裡，可把「上下相鄰or左右相鄰」的2格一起「乘-1」（正負倒過來）
# Matrix 總和最大變多大？ 「一次換2個」可移，最後剩0個或1個負號
class Solution:
    def maxMatrixSum(self, matrix: List[List[int]]) -> int:
        N = len(matrix)
        negative = total = 0  # 有幾個負數？「絕對值」總合是多少？
        minOne = inf  # 要找「絕對值」最小的數
        for i in range(N):
            for j in range(N):
                if matrix[i][j]<0: negative += 1
                total += abs(matrix[i][j])  # 先只算正的
                minOne = min(minOne, abs(matrix[i][j]))  # 「絕對值」最小
        if negative % 2 == 0: return total  # 偶數個負數，可全部變正
        else: return total - minOne - minOne  # 奇數個，讓最小的數為負
