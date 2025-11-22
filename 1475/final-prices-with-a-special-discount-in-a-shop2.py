# LeetCode 1475. Final Prices With a Special Discount in a Shop
# 特惠減價 discount 是減掉「右邊第1個遇到更便宜」的價錢，剩下多少
# 不想用「暴力2層迴圈」去試，想用「1層迴圈」配合 mono stack 算出答案
class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        N = len(prices)
        # 想知道「右邊第1個更便宜的」，那就反過來迴圈試試
        stack = []
        for i in range(N-1, -1, -1):
            now = prices[i]
            while stack and stack[-1]>now:  # 清掉太大的
                stack.pop()  # 希望 stack 對應 prices 右到左漸增
            if stack and stack[-1]<=now:  # 右邊還有更小可供折價的價錢
                prices[i] -= stack[-1]  # 折扣量
            stack.append(now)  # 現在的價錢，放入 mono stack 供折價參考
        return prices  # 回收再利用 prices 陣列
        '''
        for i in range(len(prices)):
            for j in range(i+1, len(prices)):
                if prices[j] <= prices[i]:  # 更便宜
                    prices[i] -= prices[j]  # 折扣這麼多
                    break  # 完成新的價錢，換下一個i
        return prices
        '''
