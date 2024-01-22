# i<j and nums[i]第1位數 及 nums[j] 最後位數 coprime
# coprime: 互質，即 gcd 為 1
class Solution:
    def countBeautifulPairs(self, nums: List[int]) -> int:
        def gcd(a,b): # 找最大公因數，以便判斷「互質」
            if a==0: return b
            if b==0: return a
            return gcd(b, a%b)
        
        ans = 0
        N = len(nums)
        for i in range(N): # 左手i
            for j in range(i+1,N): # 右手j
                # 先找出 nums[i] 的最高位
                a = nums[i]
                while a>=10: # 會算出 a 的最高位
                    a = a // 10
                b = nums[j] % 10 # 會算出 b 的個位數
                if gcd(a, b)==1:
                    ans += 1 # 找到1組
        return ans
