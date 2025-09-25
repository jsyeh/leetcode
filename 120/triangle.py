# LeetCode 120. Triangle
# 陣列像「三角形」一樣，每層的數量 1,2,3,4 慢慢加大。
# 請從上到下走，找到「加起來最小」的路徑。最多200層，暴力試完即可
class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        N = len(triangle)  # 先知道「三角形」層數
        @cache  # 可巧妙利用「函式呼叫函式」來解這一題
        def helper(i,j):  # 想知道第i層、第j格「往下走」最小是多少
            if i==N-1: return triangle[i][j]  # 最下層終點，直接結束
            # 利用「函式呼叫函式」把大問題「這層」變成小問題「下一層2選1」
            return triangle[i][j] + min(helper(i+1,j), helper(i+1,j+1))
        return helper(0,0)  # 從頭開始問，找到答案
