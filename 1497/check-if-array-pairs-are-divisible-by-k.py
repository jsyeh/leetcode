# LeetCode 1497. Check If Array Pairs Are Divisible by k
# 把 arr 兩兩1組，全部「能被k整除」
class Solution:
    def canArrange(self, arr: List[int], k: int) -> bool:
        counter = Counter()  # 用 Counter() 統計 %k 的量
        for num in arr:  # 對每個數逐一處理
            now = ((num%k)+k)%k# 要小心「負數」，所以加大
            counter[now] += 1  # %k 的對應 counter +1
        # print(counter)
        # 要小心 Counter({0: 50043, 1: 49957}) 是 False
        for c in counter:  # 針對 counter 逐一處理
            # 0 可以不用處理，其他必須「成雙出現」
            if c==k-c and counter[c]%2!=0:
                return False  # 自己無法成雙，且非偶數
            if c!=0 and counter[c]!=counter[k-c]:
                return False  # 無法「成雙出現」就失敗
        return True
