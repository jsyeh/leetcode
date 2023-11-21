# 找出所有的 a + rev(b) == b + rev(a) 有幾組，有用到剝皮法
# 但是不能暴力去試，因 10^5 * 10^5 很大
# a + rev(b) == b + rev(a)
# a - rev(a) == b - rev(b)
# 觀察它的規律 a - rev(a) 的diff值，去查dict即可
# 相同 diff 值的 index 查看排列組合的組合數，答案可能太多，要 MOD 10**9+7
# 註：nums 裡可以有重覆的數字
class Solution:
    def countNicePairs(self, nums: List[int]) -> int:
        def rev(n:int)->int:
            ans = 0
            while n>0: # 剝皮法，找出 rev(n) 的值
                ans = ans * 10 + n%10
                n = n // 10
            return ans

        # 先把全部的 a - rev(a) 都加到到 diff 字典裡
        diff = defaultdict(list)
        for i,a in enumerate(nums):
            d = a - rev(a)
            diff[d].append(i)

        # 再看有多少的排列組合
        ans = 0
        for k in diff: # 把字典裡有重覆的，去看排列組合的組合數
            L = len(diff[k]) # 假設有3個數相同，就C(3,2)
            # 所以是 C(L,2) 在 L 個數中，取2個數的組合數
            ans = (ans + L*(L-1)//2) % 1000000007
        return ans
