# LeetCode 3542. Minimum Operations to Convert All Elements to Zero
# 想把全部的 nums 都變成 0，步驗是「每次取一段」把它們都減同一個數，最少要幾步
# 這個題目，看起來很像 Mono stack 可解的問題，就庫存「漸漸增加」
# 下個數太小的話，就「溜滑梯」式的丟掉庫存，因為無效了。
# 有增加的話，就要再增加一次「區段減法」的步驟 ans += 1
class Solution:
    def minOperations(self, nums: List[int]) -> int:
        stack = []  # 裡面放「步步高昇」曾經停留過的數
        ans = 0
        for num in nums:
            while len(stack)>0 and stack[-1] > num:  # 降下來了，庫存無效
                stack.pop()  # 就持續吐掉庫存
            if num==0:  # 運氣好，剛好是「什麼都不用減、現成的 0
                continue
            if len(stack)==0 or stack[-1] < num:  # 不夠大，要加入 stack
                stack.append(num)
                ans += 1  # 要多一步
        return ans
