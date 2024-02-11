# 有個 MxN 個 box, 有石頭# 有阻擋物* 有空格.
# 順時針轉90度後，有些石頭# 會往下掉
# 其實等價於：先把石頭往右移，再轉動90度
class Solution:
    def rotateTheBox(self, box: List[List[str]]) -> List[List[str]]:
        M, N = len(box), len(box[0])

        for i in range(M): # 逐行處理
            rightMost = N-1 # 右邊界
            for j in range(N-1, -1, -1): # 由右到左，看能不能「往右掉」
                if box[i][j]=='#': # 石頭要「往右掉」
                    box[i][j] = '.' # 變成空格
                    box[i][rightMost] = '#'
                    rightMost -= 1 # 塞滿，下格在左邊
                elif box[i][j]=='*': # 阻擋物
                    rightMost = j - 1 # 再左邊1格才能放
        # 移好後，再轉動90度 （我之前有在FB貼過影片教學）
        return [[box[i][j] for i in range(M-1,-1,-1)] for j in range(N)]
