# LeetCode 1769. Minimum Number of Operations to Move All Balls to Each Box
# 字串 boxes 對應 n 個盒子（0空的、1有球）。若想分別「將球集中」在某個盒子，要分別移動幾步呢？
# 因盒子較少1000個，真的用暴力法，也能及時算完。
class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        ans = []
        N = len(boxes)
        for i in range(N):  # 目的地：盒子 i
            now = 0
            for j in range(N):  # 其他盒子全部巡一輪
                if boxes[j]=='1':  # 盒子 j 裡有球，要移到 box i 的話
                    now += abs(j-i)  # 從 box j 移到 box i 的距離
            ans.append(now)
        return ans
