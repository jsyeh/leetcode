# LeetCode 2601. Prime Subtraction Operation
# 有一堆數，每次「挑1個」沒挑過的數，把它減掉更小的「質數」
# 減多次後，能不能讓 nums[i] 變「嚴格遞增數列」？
# 用 greedy 方法，從左到右「想辦法」讓「左右兩項「增加量」儘量少」就好了
# greedy 就是「你想到一種方法，合乎題目要求、儘量照著做，答案就出來了」
class Solution:
    def primeSubOperation(self, nums: List[int]) -> bool:
        prime = [True] * 1001  # 先建出全部的質數
        for i in range(2,1001):  # 利用「篩子法」刪掉「質數」的倍數
            if prime[i]:  # 如果 i 是質數
                for k in range(i*i, 1001, i):  # 把i的倍數都刪掉
                    prime[k] = False

        def findPrimeBelow(now):  # 找到「比now小」的質數，以便用來「扣掉」nums[i]
            for i in range(now-1, 1, -1):
                if prime[i]: return i  # 找到比 now 小的質數
            return 0  # 找不到比 now 小的質數，就沒辦法「扣掉」，就不要減囉！

        nums[0] -= findPrimeBelow(nums[0])  # 好的開始，先「扣掉」質數，減少nums[0]
        for i in range(1, len(nums)):  # 接下來的數 nums[i] 都要比 nums[i-1] 大
            nums[i] -= findPrimeBelow(nums[i]-nums[i-1])  # 左右兩項「增加量」儘量少，扣掉「差額」內的質數
            if nums[i] <= nums[i-1]: return False  # 扣掉差額內的質數，還無法完成任務（嚴格遞增），就失敗
        return True  # 順利走到最後，成功了!
