# LeetCode 2481. Minimum Cuts to Divide a Circle
# 切圓經過圓心：可沿直徑「對半切」，也可沿半徑「圓心往外切」。要切幾刀「n等分」
class Solution:
    def numberOfCuts(self, n: int) -> int:
        # 如果是 2 的倍數，可以「對半切」
        if n==1: return 0  # 1個人，不用切
        if n==2: return 1  # 對半切，平分給2個人
        if n==3: return 3
        if n==4: return 2  # 兩次「對半切」
        if n==5: return 5
        if n==6: return 3  # 三次「對半切」
        if n==7: return 7
        if n==8: return 4  # 四次「對半切」
        if n==9: return 9
        if n==10: return 5  # 五次「對半切」
        if n==11: return 11
        if n==12: return 6
        # 觀察後，發現就3種可能
        if n%2==0: return n//2
        else: return n
