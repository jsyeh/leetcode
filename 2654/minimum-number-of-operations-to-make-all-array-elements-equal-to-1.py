# LeetCode 2654. Minimum Number of Operations to Make All Array Elements Equal to 1
# 要把 nums 陣列裡，全部都變成1，方法是「相鄰2數」挑一個改成「最大公因數」，要做幾次？
# 關鍵在「相鄰2數互質」，就可做出「第1個1」接下來就可以「量產1」了。
class Solution:
    def minOperations(self, nums: List[int]) -> int:
        N = len(nums)
        ones = nums.count(1)  # 先數有幾個1，好的開始
        if ones>0:  # 最簡單「完成任務」的方法，只要有1，就可感染，讓其他數「都變成1」
            return N - ones  # 剩下「不是1的」都能用 gcd(x,1)=1量產成1
        # 接下來，「能不能找到某一段」最大公因數會是1
        ans = inf  # 無限大，代表「做不到」、無法得到「最大公因數」是1
        for i in range(N):  # 某一段的開頭
            g = nums[i]  # 想找這段的 gcd 最大公因數
            for k in range(i+1, N):  # 某一段的結尾 i...k
                g = gcd(g, nums[k])  # 繼續計算「最大公因數」
                if g==1:  # 太好了，這段的最大公因數是1，量一下長度
                    ans = min(ans, k-i)  # 經過k-i次「最大公因數」操作，可得到第1個1
                    break
        if ans==inf: return -1  # 完全「做不到」
        return ans + N - 1
