# LeetCode 1296. Divide Array in Sets of K Consecutive Numbers
# 有一堆數字，問能不能分成一堆「連續k個數字」
class Solution:
    def isPossibleDivide(self, nums: List[int], k: int) -> bool:
        queue = deque()  # queue 存「何時、降多少」
        prev, amount = -1, 0  # 記錄「前一個數字是誰、要幾個」以便找「連續數字」的量
        nums = sorted(Counter(nums).items())  # 數字數個數，再「小到大」排好
        for num, cnt in nums:  # 每組數字「是誰、有幾個」
            if amount>cnt: return False  # 需要數目，但不夠，失敗
            if amount>0 and prev+1!=num: return False  # 有需要數目，但數字不連續，失敗
            if cnt>amount: queue.append((num+k,cnt-amount))  # 需更多數目，記錄下來
            amount = cnt
            prev = num
            if len(queue)>0 and queue[0][0]<=num+1:  # 記錄的時間到了
                amount -= queue.popleft()[1]  # 數字要還原/降下去
        if len(queue)>0: return False  # 數字用完，卻還有需要的數，失敗
        return True  # 最後成功
