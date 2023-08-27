# 可使用爬山的演算法，找到 local maximum 即可
# 也就是根據梯度趨勢，往高處走
# 但「慢慢走」太慢了，可用 binary search加速
# 左右決定 mid column, 找出 mid column 裡最大值，再決定往左or往右走
class Solution:
    def findPeakGrid(self, mat: List[List[int]]) -> List[int]:
        M, N = len(mat), len(mat[0])
        left, right = 0, N-1 # 因左右都包含，所以會夾擊到中間
        while left<=right: # 因左右都包含，所以會夾擊到中間
            mid = (left+right)//2
            bestI = 0 # 固定 col 為 mid，上下去找最好 i 值
            for i in range(M): 
                if mat[i][mid] > mat[bestI][mid]:
                    bestI = i
            # 現在上下來說是最大，接下來看 mid 要往左右哪個方向移
            leftBig = mid-1>=0 and mat[bestI][mid-1] > mat[bestI][mid]
            rightBig = mid+1<N and mat[bestI][mid+1] > mat[bestI][mid]
            if (not leftBig) and (not rightBig):
                return [bestI, mid] # 找到最大的位置
            if leftBig: # 往左走
                right = mid - 1
            if rightBig:
                left = mid + 1
        return [0, 0] # 隨便給個值吧，應該一定找得到，不會走到這行
# case 49/54: [[10,30,40,50,20],[1,3,2,500,4]]
