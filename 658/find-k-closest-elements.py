# 要在 arr 裡，找出 k 個數，最接近x。如果有2個數與x的距離一樣時，小的數較接近
class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        # 先 binary search 找到最接近 x 的位置
        # 接著，左右擴張，得到答案
        N = len(arr)
        if k == N: return arr # 全部都撿來用

        left, right = 0, N # 右不包含
        while left < right:
            mid = (left+right) // 2
            if arr[mid] == x:
                left = mid
                break
            if arr[mid] < x:
                left = mid + 1
            if arr[mid] > x:
                right = mid
        # print("left:", left) # 這是最接近 x 的位置，想像成「稍微偏左」

        left, right = left, left # 要左右逼近，右包含
        # 上面有個問題：如果 arr[left] 不是最佳解，卻被強加 arr[left]
        if left>0 and left<=N-1 and x-arr[left-1]<=arr[left]-x:
            left,right = left-1, left-1

        while right-left+1<k: # 若還沒湊齊 k 個數
            if left == 0: # 撞到左邊界
                right = left + k - 1
                break
            if right >= N-1: # 撞到右邊界
                right = N - 1
                left = right -k + 1
                break
            # 經過上面兩個測試後，保證還沒有碰到邊界，便能做下面操作

            if arr[right+1] - x < x - arr[left-1]:
                right += 1 # 右邊比較近，要往右邊長
            else: left -= 1

        if right == N-1: return arr[left:]

        return arr[left:right+1]
# case: 63/67: [0,0,1,2,3,3,4,7,7,8] 3 5
# 問題掉在 4-7中間的5,right(7)不能用啊
# case 64/67: [1,3] 1 2
