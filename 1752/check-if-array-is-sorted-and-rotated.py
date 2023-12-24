# 檢查 nums 是否「小到大」排序好，或著「稍微轉一下」
# 像 3,4,5,1,2 就是有轉過，也是成功。
# 小心 6,6,10 是正確的 6 10 6 也是正確的
# 可以先找到最小值的i,再從 range(i-N+1,i) 兩兩比對
class Solution:
    def check(self, nums: List[int]) -> bool:
        N = len(nums)
        # 看了 lee215 的解題思緒，簡單很多。照著寫寫看
        bad = 0 # 有發生幾次逆轉？
        for i in range(-1,N-1): # 全部檢查，超過邊界也行
            # 剛好 nums[-1]是最右邊，用了這個性質
            if nums[i] > nums[i+1]: # 有逆輚問題
                bad += 1 # 逆轉
        if bad > 1: return False # 超過1次以上，就失敗
        else: return True # 正常下只會有一次逆轉，成功
        ''' # 下面的寫法不好、有錯、不易理解，上面重寫
        minI = 0
        for i in range(N):
            if nums[i] < nums[minI]:
                minI = i
        # 找到最小的 minI 後，再做一次檢查
        #print(minI-N, minI-1) # 右少1格，才能 i i+1比較
        for i in range(minI-N, minI-1):
            if nums[i]>nums[i+1]: # 沒有遞增，就失敗
                return False
        return True
        '''
# case 62/108: [1,1,1] # 哇，不用嚴格遞增，相同也可以
# case 104/108: [6,10,6] # 這也可以，minI 不好找
