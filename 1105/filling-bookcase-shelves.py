# LeetCode 1105. Filling Bookcase Shelves
# books 裡有每本書的「寬、高」，書架的寬度固定，問「會有多高？」
# 看起來 DP 動態規劃能解這題。
# 方法1：使用Bottom-Up DP 建立陣列，來解這題。
# 方法2：使用「函式呼叫函式」的 DP 方法，來解這題
class Solution:
    def minHeightShelves(self, books: List[List[int]], shelfWidth: int) -> int:
        N = len(books)
        table = [inf]*(N+1)  # table[i] 只使用前i本書，答案是多少
        table[0] = 0  # 0本書，答案是0
        for i in range(1,N+1):  # 要試著放1本、2本...N本書，更新table[1]...table[N]
            thisWidth, thisHeight = 0, 0 # 最新的一層，寬度、高度 先對應 0, 0
            # 放i本書，最後那本是i-1，用倒過來的迴圈，往前收集「同一層」
            for k in range(i-1,-1,-1):  # 處理「最新一層」的答案
                thisWidth += books[k][0]  # 更新寬度
                thisHeight = max(thisHeight,books[k][1])  # 更新高度，以最高那本為主
                if thisWidth>shelfWidth: break  # 如果寬度超過一層的寬度，就離開
                # 前面有k本書(0...k-1) 是在上方舊書架，對應最佳高度 table[k]
                # 最新一層(k...N-1) 這幾本，對應高度是 thisHeight，上下兩個加起來，是一種可能
                table[i] = min(table[i], table[k] + thisHeight) # 嘗試更新答案
        return table[N]  # 放 N 本書，最好的答案
