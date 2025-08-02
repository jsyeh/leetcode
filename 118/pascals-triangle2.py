# LeetCode 118. Pascal's Triangle
# 數學的「巴斯卡三角形」的計算方式，是從上方的「2項相加」
class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        ans = []
        ans.append([1])
        for i in range(numRows-1):
            now = [1]  # 最左邊的 1
            #for k in range(i):  # 方法1: 如果 k 從 0 開始
            #    now.append( ans[-1][k] + ans[-1][k+1])
            for k in range(1,i+1):  # 方法2: 如果 k 從 1 開始
                now.append( ans[-1][k-1] + ans[-1][k] )  
                # 從「前一筆」推出來
            now.append(1)  # 最右邊的 1
            ans.append(now)
        return ans
        # 可用下面程式來理解、想像
        ans = []
        ans.append([1])
        ans.append([1,1])  # i:0
        ans.append([1,2,1])  # i:1
        ans.append([1,3,3,1])  # i:2
        ans.append([1,4,6,4,1])  # i:3 numRows:5
        return ans


        ans = []
        ans.append([1])
        for i in range(numRows-1):
            now = [1]
            for k in range(1, i+1):
                now.append( ans[-1][k-1] + ans[-1][k])
            now.append(1)
            ans.append(now)
        return ans
