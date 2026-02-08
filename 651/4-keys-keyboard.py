# LeetCode 651. 4 Keys Keyboard
# 鍵盤只有 4 種鍵：正常鍵A、Ctrl-A全選、Ctrl-C複製、Ctrl-V貼上
# 你只能按 n 次，請問能做出的「最長字串」有多長？
class Solution:
    def maxA(self, n: int) -> int:
        # 有3種可能：按A、Ctrl-A Ctrl-C Ctrl-V、之前大小Ctrl-V
        @cache
        def helper(n):
            # if n==1: return 1  # 按1個'a'
            # if n==2: return 2  # 按2個'a'
            # if n==3: return 3  # 按3個'a'
            # if n==4: return 4  # 按4個'a'
            # if n==5: return 5  # 按5個'a'
            # if n==6: return 6  # 按6個'a' 或 3個'a'再Ctrl-A Ctrl-C CtrlV
            # 以上6行，可簡化成 if n<=6: return n
            if n<=6: return n
            # 接下來，要享受「全選、複製、貼上」加速的過程
            return max(helper(n-3)*2, helper(n-4)*3, helper(n-5)*4)
        return helper(n)
