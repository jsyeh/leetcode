# LeetCode 1861. Rotating the Box
# 要轉動盒子，裡面的 石頭# 會往下掉，但會被 牆* 擋住
# 只要會用 for 迴圈 + 陣列，就可以寫這題了
class Solution:
    def rotateTheBox(self, box: List[List[str]]) -> List[List[str]]:
        M, N = len(box), len(box[0])
        ans = [[box[i][j] for i in range(M-1,-1,-1)] for j in range(N)]
        for i in range(N-1,-1,-1):
            for j in range(M):
                if ans[i][j]=='#':
                    ans[i][j] = '.'
                    for ii in range(i,N+1):
                        if ii>=N or ans[ii][j]=='#' or ans[ii][j]=='*':
                            ans[ii-1][j] = '#'
                            break
        return ans
