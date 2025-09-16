# LeetCode 2197. Replace Non-Coprime Numbers in Array
# 將 nums 裡「相鄰」「沒互質gcd>1」的2數「合併成1個數」。
# gcd() 可快速測「互質」的狀況，若 gcd()>1，就可以消掉
# 但可能「中間的數，與右邊結合後」，可回頭與左邊的數「再結合」
# Hint 說，就「左到右」慢慢來，再看「是否要與左邊的數合併」可用 stack 的 push/pop 觀念
class Solution:
    def replaceNonCoprimes(self, nums: List[int]) -> List[int]:
        ans = [ nums[0] ]  # 先放「最左邊的數」開始，下面每次與 ans[-1] 測合併
        for i in range(1, len(nums)):  # Hint 1: 左到右、慢慢來
            g = gcd(ans[-1], nums[i])  # 看「最大公因數gcd」的值
            if g > 1:  # 可消 gcd > 1
                ans[-1] = ans[-1] * nums[i] // g  # 更新資料
                while len(ans)>1 and gcd(ans[-1],ans[-2])>1:  # 可與左邊的數合併
                    now = ans.pop()  # 先備份「將消掉」的最後一筆
                    ans[-1] = ans[-1] * now // gcd(ans[-1], now)  # 更新、塞回去合併
            else: ans.append(nums[i])  # 不可消，就直接塞
        return ans
