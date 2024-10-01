# LeetCode 1497. Check If Array Pairs Are Divisible by k
# 把 arr 兩兩1組，全部「能被k整除」
class Solution:
    def canArrange(self, arr: List[int], k: int) -> bool:
        freq = [0] * k  # 這次改用「陣列」來解，存 %k 的結果
        for num in arr:  # 對每個數逐一處理
            freq[(num%k+k)%k] += 1# 要小心「負數」，所以加大
        print(freq)
        if k%2==0 and freq[k//2]%2!=0:  # ex. k=4時 2 無法與別人一組
            return False  # 所以自己要偶數，不然就失敗
        if freq[0]%2!=0:  # 0只能自己湊偶數，不然就失敗
            return False
        for i in range(1,k//2+1):  # 針對前半，逐一處理，必須「成雙出現」
            if freq[i]!=freq[k-i]:  # 對應的數，數目不同，就失敗
                return False
        return True
