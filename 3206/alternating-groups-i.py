# LeetCode 3206. Alternating Groups I
# 環狀磚塊：0紅色 1藍色，任3個相鄰「色彩相間」很棒，有幾個？
class Solution:
    def numberOfAlternatingGroups(self, colors: List[int]) -> int:
        ans = 0
        for i in range(len(colors)):  # 針對每格的色彩
            # 相鄰3個不同色
            if colors[i-2]!=colors[i-1] and colors[i-1]!=colors[i]:
                ans += 1
        return ans
