# 題目看起來很簡單，就把「每一項」與其他人的「距離和」算出來即可
# 但是有 10^5 這麼多項，就無法直覺暴力算。
# 思考：有什麼可以省下來、不用重覆算的地方嗎？
#  以「距離和」為想法，「拉很多條線」會發現很多「距離」是固定的
#  和「runSum」有點關係：若小到大排好，最左-最右、次左、次右...
#  但是想想，還是很亂。偷看 Editorial
# Editorial 裡的寫法，是以每個數為準，左邊三角形 + 右邊三角形
#  配合 runSum[i] 來計算三角形的值
class Solution:
    def getSumAbsoluteDifferences(self, nums: List[int]) -> List[int]:
        N = len(nums)
        # runSum[i] 表示 nums[0]+...+nums[i]
        runSum = [0]*N
        runSum[0] = nums[0]
        for i in range(1,N):
            runSum[i] = runSum[i-1] + nums[i]
        # print(runSum)
        
        ans = [0]*N
        for i in range(N):
            left = (i+1)*nums[i] - runSum[i] 
            # 左邊距離和 = 左長方形-左下三角 （含本身）
            right = runSum[N-1]-runSum[i] - (N-i-1)*nums[i] 
            # 右邊距離和 = 右梯形-右長方形 （不含本身）
            ans[i] = left+right
        return ans
