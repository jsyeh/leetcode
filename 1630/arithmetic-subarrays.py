# 要判斷是否為「等差級數」也就是 nums[i]-nums[i-1] == nums[1]-nums[0]
# 不過題目有稍做修改, index 限定只檢查 l[i]...r[i]範圍
# 因 500個數而已, 暴力應該就算完了
# 但可惡的, 好像需要重新排序的樣子
class Solution:
    def checkArithmeticSubarrays(self, nums: List[int], l: List[int], r: List[int]) -> List[bool]:
        ans = []
        Q = len(r) # 確定問幾次
        for i in range(Q): # 逐筆詢問
            # 題目說 0<=l[i]<r[i]<N 所以不用檢查範圍
            temp = nums[l[i]:r[i]+1] # 取出範圍內的數字
            temp.sort() # 從小到大排好
            diff = temp[1] - temp[0] # 基礎差距
            bad = 0
            for k in range(r[i]-l[i]): # 在小範圍內比較
                if temp[k+1]-temp[k] != diff: # 距離不合
                    bad = 1 # 就壞掉
            if bad == 0: ans.append(True)
            else: ans.append(False)
        return ans
