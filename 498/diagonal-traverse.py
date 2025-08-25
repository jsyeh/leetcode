# LeetCode 498. Diagonal Traverse
# m x n 陣列裡，從左下到右上，再從右上到左下，z字型依序走過
class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        M, N = len(mat), len(mat[0])  # 先知道長、寬
        # ans = [0] * (M*N)  # 沒想到我用 ans.append() 會超過時間
        # 想到另外一種作法，是反過來，問 mat[i][j] 會放在哪一格
        d = defaultdict(list)
        for i in range(M):
            for j in range(N):
                d[i+j].append(mat[i][j])  # mat[i][j] 放在 i+j 層
        ans = []  # 接下來，從 d 取出全部的數，塞入答案
        for i in range(M+N-1):
            if i%2==0:  # 偶數層，左下到右上，要倒過來放
                for val in d[i][::-1]:  # 倒過來的迴圈、倒過來放 
                    ans.append(val)
            else:  # 奇數層，右上到左下，順著放
                for val in d[i]:  # 順著放
                    ans.append(val)
        return ans
