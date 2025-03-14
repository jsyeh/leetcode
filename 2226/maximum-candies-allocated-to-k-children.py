# LeetCode 2226. Maximum Candies Allocated to K Children
# candies 裡有很多堆糖果，每堆又能分很多小堆，每人只能拿1小堆，
# 希望 k 個小朋友每人拿到的那堆都一樣大堆，問每位小朋友「最多可拿到幾個糖果」
# 可用 binary search 解這題，希望寫出 helper(c) 來判斷
class Solution:
    def maximumCandies(self, candies: List[int], k: int) -> int:
        def helper(c):  # 每個小朋友「不夠拿到c個糖果」嗎？
            piles = 0  # 如果每小堆有c個糖果，能分幾堆？
            for candie in candies:  # 將每大一堆糖果
                piles += candie // c  # 分成 canie // c 堆
            return piles < k  # 是否「不夠」（堆數不夠）
        # 讓上面 helper() 輸出 False ... True ... 
        # 而第一個 True 的左邊，就是「夠」的最大值
        return bisect_left(range(1,sum(candies)+1), True, key=helper)
