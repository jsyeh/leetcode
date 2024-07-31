# LeetCode 1105. Filling Bookcase Shelves
# books 裡有每本書的「寬、高」，書架的寬度固定，問「會有多高？」
# 看起來 DP 動態規劃能解這題。
# 方法1：使用Bottom-Up DP 建立陣列，來解這題。
# 方法2：使用「函式呼叫函式」的 DP 方法，來解這題
class Solution:
    def minHeightShelves(self, books: List[List[int]], shelfWidth: int) -> int:
        @cache
        def helper(n):  # 想知道「如果有n本書」，那答案是多少
            if n == 0: return 0  # 0本書，不用任何高度（終止條件）
            ans = books[n-1][1] + helper(n-1)  # 如果這本書獨立放一層，總高度這麼多
            nowWidth, nowHeight = books[n-1][0], books[n-1][1] # 目前這層的寬度、高度
            for i in range(n-2, -1, -1):  # 如果與其他書同一層，有機會更小嗎
                if nowWidth + books[i][0]>shelfWidth: break  # 若寬度超過，那就別再算了
                nowWidth += books[i][0]  # 往前多一本當鄰居，這層的寬度增加了
                nowHeight = max(nowHeight, books[i][1])  # 更新目前高度（多一本，可能更高）
                ans = min(ans, helper(i) + nowHeight)  # 函式呼叫函式
                # 前面放i本書（0...i-1)，這層放第i本書之後的書(i...n-1) 答案有更好嗎？
            return ans
        return helper(len(books))
