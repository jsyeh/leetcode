# LeetCode 2601. Prime Subtraction Operation
# 有一堆數，每次「挑1個」沒挑過的數，把它減掉更小的「質數」
# 減多次後，能不能讓 nums[i] 變「嚴格遞增數列」？
class Solution:
    def primeSubOperation(self, nums: List[int]) -> bool:
        prime = []  # 使用「篩子法」，收集 1000 以下的質數
        possible = [True] * 1001  # 可能是質數
        for i in range(2,1001):
            if possible[i]: 
                prime.append(i)  # 收集到質數
                for k in range(i*i, 1001, i): possible[k] = False  # 刪掉它的倍數
        def findPrimeBelow(now):
            index = bisect_left(prime, now) - 1 # 找到左邊的插入點，-1 就是「更小的值」
            if index==-1: return 0  # 沒有適合的質數
            else: return prime[index]  # 更小的質數
        
        nums[0] -= findPrimeBelow(nums[0])  # 最前面的數，先壓到最小
        for i in range(1, len(nums)):  # 剩下的數，要慢慢增加
            nums[i] -= findPrimeBelow(nums[i] - nums[i-1])  # 將「增加的幅度」壓到最小（但還是會漸增）
            if nums[i-1] >= nums[i]: return False  # 壓完後，無法成功，就失敗了
        return True  # 沒有失敗，就成功了！
