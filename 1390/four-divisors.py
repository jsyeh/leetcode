# LeetCode 1390. Four Divisors
# 剛好有4個「可整除num」的「因數」，把「因數」全部加起來
# 因數一定有1和num本身，其實就是「任2個不同質數相乘」or「質數3次方」
class Solution:
    def sumFourDivisors(self, nums: List[int]) -> int:
        isPrime = [True] * 100001  # 用質數篩子法，找10^5 以下的質數
        prime = []  # 把質數放在陣列裡，方便for迴圈「測試質數」
        for i in range(2,100001):
            if isPrime[i]:  # 是質數
                prime.append(i)  # 記下來
                for ii in range(i*i, 100001, i):  # 所有倍數都刪掉
                    isPrime[ii] = False
        ans = 0  # 找到範圍內所有質數後，就可計算答案
        for num in nums:  # 逐一檢查
            if isPrime[num]: continue  # 質數一定不是答案
            for p in prime:  # 測試質因數
                if num%p==0:  # 找到1個小的質因數，就可確認身份
                    if num == p*p: break  # 先去除「質因數的平方數」
                    if isPrime[num//p] or num==p*p*p:  # 兩種可能
                        ans += 1 + p + num//p + num  # 算入答案
                    break  # 離開「測試質因數」
        return ans
