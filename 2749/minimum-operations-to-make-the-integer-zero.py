# LeetCode 2749. Minimum Operations to Make the Integer Zero
# 把 num1 變成 0 要幾步？每次把 num1 減掉 (2^i + num2) 其中 2^i 有點像是「二進位表示法」的題目
# 每次可少掉1個1，但 - num2 可能會長出一堆1，有點麻煩。展開、移項 num - (一堆2進位) - k * num2
# num1 - k * num2 對應「做了 k 步」的差額，給 2^i 配對，若剩下的 1 數量，剛好可用 k 次消掉1，完美！
# 但若 k 更大，怎麼辦？可拆解、浪費步數 ex. 4可1次，2+2可2次，2+1+1可3步，1+1+1+1可4步
# 只要介於「有幾個1」到「全部用1湊全部的數」都能做到：target.bit_count() <= k <= target 即可
# Hint 3 說，最多只要60次操作，便可確定「是否做得到」 
class Solution:
    def makeTheIntegerZero(self, num1: int, num2: int) -> int:
        for k in range(1, 61):  # 要看「幾步」能做到，最多60步
            target = num1 - k * num2  # 差額，能用 2^i 配出來嗎？
            # 有機會：  「有幾個1」   到   「全部用1湊全部的數」
            if target.bit_count() <= k <= target:
                return k  # 恭喜 k 步就做到了
        return -1  # 試了全部可能，卻都做不到，失敗！
