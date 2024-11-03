# LeetCode 796. Rotate String
# 如果2字串是旋轉的字串，就 True。暴力法，就可以完成
class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        N = len(s)  # 字串的長度
        if N != len(goal): return False  # 兩字串長度若不同，一定有錯
        for d in range(N):  # 先決定「兩字串」可能「差幾格」的距離，照這距離比較
            bad = False  # 小迴圈前面，一開始還沒壞
            for i in range(N):  # 要累積一堆好的
                if s[i] != goal[(i+d)%N]:  # 照這次的距離比較，卻沒能對好
                    bad = True  # 這次壞了（小迴圈中間比較）
                    break  # 如果壞了，就提早結束這回合，可以加速/不浪費時間哦！
            if bad==False: return True  # 小迴圈後面，如果這次沒壞，就成功了
        return False
