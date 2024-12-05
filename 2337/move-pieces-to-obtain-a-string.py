# LeetCode 2337. Move Pieces to Obtain a String
# L左移 R右移 _空格，問 start 能不能變成 target
class Solution:
    def canChange(self, start: str, target: str) -> bool:
        # 本來我想要做 BFS 模擬，但發現太慢&花太多空間
        # 有人分享用 start[i] vs. target[j] 來比對，用 2 個index i,j 看能不能走完
        # 如果 start[i] 和 target[j] 都是 'R' 那需要 i<=j 才能右移 
        # 如果 start[i] 和 target[j] 都是 'L' 那需要 j<=i 才能左移
        N = len(start)  # 兩字串長度相同，都是 N
        i = j = 0  # 一開始都在左邊，準備開始
        while i<N or j<N:  # 只要還沒有走到底，就繼續做
            while i<N and start[i]=='_':  # 避開全部的空格，離開while迴圈代表「找到字母」或超線
                i += 1
            while j<N and target[j]=='_':  # 避開全部的空格，離開while迴圈代表「找到字母」或超線
                j += 1
            if i==N and j==N: return True  # 成功走完
            if i==N or j==N: return False  # 有1個走完、1個沒走完，失敗
            if start[i]==target[j]=='R' and i<=j:  # 可右移走到
                i, j = i+1, j+1  # 順移往下一筆走
            elif start[i]==target[j]=='L' and j<=i:  # 可左移走到
                i, j = i+1, j+1  # 順移往下一筆走
            else: return False  # 都不是，就失敗
        return False
