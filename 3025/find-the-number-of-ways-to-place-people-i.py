# LeetCode 3025. Find the Number of Ways to Place People I
# points 裡有許多 (x,y)，有幾種「左上、右下」的2點組合（框出方形中沒其他點）
# 因「點數少」又「座標少」所以暴力檢查即可。小心「y座標」是用數學的座標，原點在「左下角」
class Solution:
    def numberOfPairs(self, points: List[List[int]]) -> int:
        N = len(points)
        pt = points  # 為了讓程式變數「短一點」，換一下變數名
        ans = 0  # 收集「有幾種」左上、右下的組合
        for i in range(N):  # (希望是)左上點
            for j in range(N):  # (希望是)右下點
                if i==j: continue  # 避開「自己」
                if pt[i][0] > pt[j][0] or pt[i][1]  < pt[j][1]:  # 小心「y座標」
                    continue  # 避開「非」「左上、右下」的點
                for k in range(N):  # 有沒有第3點在裡面
                    if k==i or k==j: continue  # 避開「左上、右下」的點
                    if pt[i][0] <= pt[k][0] <= pt[j][0] and pt[i][1] >= pt[k][1] >= pt[j][1]:
                        break  # points[i] 和 points[j] 裡，夾了1個點 points[k]  # 小心「y座標」
                else: ans += 1  # 最後沒有壞掉、找到1組答案
        return ans
