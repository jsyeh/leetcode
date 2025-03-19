# LeetCode 3191. Minimum Operations to Make Binary Array Elements Equal to One I
# 想把 nums 裡的數，每次「切換3個相鄰的數」0與1互換，要全部「變成1」 問需要「切換幾次」
class Solution:
    def minOperations(self, nums: List[int]) -> int:
        ans = 0  # 切換的次數，迴圈前面是0
        for i in range(len(nums)-2):  # 迴圈裡，從左到右巡一輪（下面+2 這裡就-2）
            if nums[i]==0:  # 遇到 0 就要切換
                ans += 1  # 加1次
                nums[i] = 1  # 變成1
                nums[i+1] = 1 - nums[i+1]  # 0與1互換
                nums[i+2] = 1 - nums[i+2]  # 0與1互換
        # 離開迴圈時，檢查「最後2個」是否有殘留0，有殘留的話，就失敗
        if nums[-1]==0 or nums[-2]==0: return -1
        return ans  # 沒有殘留0、全部都是1的話，任務完成，切換的次數 ans 次
