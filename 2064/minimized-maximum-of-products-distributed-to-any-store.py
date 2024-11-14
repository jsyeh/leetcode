# LeetCode 2064. Minimized Maximum of Products Distributed to Any Store
# 每家店只賣1種商品。有 n 家店，m 種商品的數量 quantities 
# 要怎麼分，讓店裡放的商品越少越好？（店裡不要屯積太多商品）
# 這題剛好適合用 Binary Search 來找答案/猜出答案。
class Solution:
    def minimizedMaximum(self, n: int, quantities: List[int]) -> int:
        # 其實就是 n 家店，怎麼平分 m 種商品。
        def possible(perShop):  # 每家店「最多放perShop商品」，「可能嗎？」
            shops = 0  # 需要幾家店呢？
            for q in quantities:
                shops += q // perShop  # q商品，要放要幾家店？
                if q%perShop: shops += 1  # 有餘的話，再加1家店
            if shops <= n: return True  # 所需 shops 數，n 家店足夠，太好了
            else: return False  # 不夠的話 false

        max_q = max(quantities)
        ans = bisect_left(range(1,max_q),1, key=lambda x: possible(x))
        return ans+1
