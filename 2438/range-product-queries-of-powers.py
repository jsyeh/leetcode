# LeetCode 2438. Range Product Queries of Powers
# 一堆 2 的很多次方「加起來是n」的話，小到大放入 power 陣列 其實就是 n 的二進位 bits 嘛！
# 再把 queries[i] = [left,right] 算出 power[left] * ... * power[right] 的結果
class Solution:
    def productQueries(self, n: int, queries: List[List[int]]) -> List[int]:
        power = []  # 要算出 n 對應的 power 陣列
        one = 1  # 這個變數，依序變 1,2,4,8,16,32,64...
        while n > 0: # 先用「剝皮去」變出二進位
            if n % 2 == 1:  # 對應 bit 是 1
                power.append(one)  # 就把對應的 2 的很多次方的值，加到 power 陣列裡
            n = n // 2
            one = one * 2  # 二進位的位數，依序變 1,2,4,8,16,32,64...
        MOD = 10**9+7  # ans 裡數字太大，要取餘數
        ans = []  # 要把 queries 裡的答案，依序放入 ans 裡
        for left, right in queries:  # 左右的範圍
            now = 1  # power[i] 會視範圍「乘入 now 裡」
            for i in range(left, right+1):
                now = now * power[i] % MOD  # power[i] 會視範圍「乘入 now 裡」
            ans.append(now)  # 乘好後，會放入 ans 裡
        return ans
