# LeetCode 1975. Maximum Matrix Sum
# 可把任2項相鄰的數「乘上-1」，問能做出「最大」的加總結果
# 要「加起來最大」，就是「儘量把負數變少」Hint 1 建議「每個row只留1個負數」
# Hint 2 說，如果整個matrix裡「只有1個負數」，就無法變正的
# 以上可推論：負數的位置，可「慢慢移動」到最小的那個數，或是全變正的
class Solution:
    def maxMatrixSum(self, matrix: List[List[int]]) -> int:
        negative = 0  # 矩陣裡，有幾個「負數」
        totalAbs = 0  # 全部變「正的」加起來的值
        smallest = inf  # 要找最小值，所以初始值設「正無限大」
        for row in matrix:
            for i in range(len(row)):
                if row[i]<0:
                    negative += 1  # 數一數，有幾個「負數」
                    row[i] = -row[i]  # 都先變成正的哦！
                totalAbs += row[i]  # 若全部都變正的數，全部變「正的」加起來的值
                smallest = min(smallest, row[i])  # 「絕對值最小」的數
        if negative%2==1: # 若「負數」有單數個，那就讓「絕對值最小」的數來當
            return totalAbs - 2*smallest  # 答案就「全正的」-「最小那個」2次
        return totalAbs  # 若「負數」有偶數個，就能全部變成「正的」
