# 要做 smooth filter 是影像處理常做的操作。
# 在邊邊角角的地方，可能無法做滿，就只用少少的部分來做
# 另外 int 整數，平均時要去除小數部分 //count
class Solution:
    def imageSmoother(self, img: List[List[int]]) -> List[List[int]]:
        M, N = len(img), len(img[0])
        ans = [[0]*N for _ in range(M)]

        for i in range(M):
            for j in range(N):
                i0, j0 = max(i-1, 0), max(j-1, 0) # 上、左邊界，右不包含
                i1, j1 = min(i+2, M), min(j+2, N) # 下、右邊界，右不包含
                total = 0
                for ii in range(i0,i1): # 每種不同的ii
                    total += sum(img[ii][j0:j1]) # 把全部 jj 對應值加起來
                ans[i][j] = total // (i1-i0) // (j1-j0) # 算出平均值
        return ans
