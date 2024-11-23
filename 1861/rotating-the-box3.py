# LeetCode 1861. Rotating the Box
# 要轉動盒子，裡面的 石頭# 會往下掉，但會被 牆* 擋住
# 只要會用 for 迴圈 + 陣列，就可以寫這題了
class Solution:
    def rotateTheBox(self, box: List[List[str]]) -> List[List[str]]:
        M, N = len(box), len(box[0])
        ans = [[box[i][j] for i in range(M-1,-1,-1)] for j in range(N)]  # 先轉動90度變ans矩陣
        for j in range(M):  # 左到右，每一個 column 都去巡
            lowest = N-1  # 記錄「最下面」的位置
            for i in range(N-1,-1,-1):  # 從下往上巡
                if ans[i][j]=='#':  # 遇到石頭
                    ans[i][j] = '.'  # 舊位置先清空
                    ans[lowest][j] = '#'  # 石頭放在「最下面」的位置
                    lowest -= 1  # 石頭會佔一格，「最下面」的位置，會往上移
                elif ans[i][j] == '*':  # 遇到障礙物，也要更新「最下面」的位置
                    lowest = i-1  # 「它」的上一格 
        return ans
