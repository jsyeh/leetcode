# LeetCode 796. Rotate String
# 如果2字串是旋轉的字串，就 True。暴力法，就可以完成
class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        N1, N2 = len(s), len(goal)
        if N1 != N2: return False

        for d in range(N1):  # 先決定「兩字串」可能「差的距離
            bad = False  # 小迴圈前面，一開始還沒壞
            for i in range(N1):
                if s[i]!=goal[(i+d)%N1]:  # 這次沒能對好，壞了
                    bad = True  # 這次壞了
                    break  # 如果壞了，就提早結束這回合，可以加速/不浪費時間哦！
            if bad==False: return True  # 小迴圈後面，如果這次沒壞，就成功了
        return False
