# LeetCode 1475. Final Prices With a Special Discount in a Shop
# prices[i] 特價規則：減掉「右邊第1個<=它」的數
class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        # 直接回收利用 prices 當答案
        for i in range(len(prices)):  # 針對每個價錢
            for j in range(i+1, len(prices)): # 往右查
                if prices[i]>=prices[j]:  # 右邊第1個<=它的數
                    prices[i] -= prices[j]  # 減掉它
                    break  # 完成這回合，換下一個i
        return prices
        
