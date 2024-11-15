# LeetCode 2107. Number of Unique Flavors After Sharing K Candies
# candies[i] 是口味，把「連續k個糖果」給妹妹後，自己最多有幾種「不同口味」的糖果
# 利用 sliding window 來解決這題，
class Solution:
    def shareCandies(self, candies: List[int], k: int) -> int:
        counter = Counter()  # 用 Counter()快速知道有幾種「不同口味」的糖果
        N = len(candies)
        for i in range(k,N):  # 「最前面k個」給妹妹，統計「k後面」的糖果
            counter[candies[i]] += 1
        ans = len(counter)

        for i in range(N-k):  # 開始滑動
            counter[candies[i]] += 1  # 左邊還回來
            counter[candies[k+i]] -= 1  # 右邊送出去
            if counter[candies[k+i]]==0:  # 若減少後，變成0
                del counter[candies[k+i]]  # 就把這個刪掉，讓len()正確
            ans = max(ans, len(counter))  # 更新答案
        return ans
        
