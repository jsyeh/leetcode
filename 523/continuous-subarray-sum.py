# 判斷 good subarray： 長度2以上，且 sum 是 k 的倍數
# sum 就用 prefix 來算吧!
# 想要更快的話，我參考 compton_scatter 的解法，用 %k 來存prefixSum
# 利用 set() 看 %k 的值是否重覆出現，有的話，就是成功、有k的倍數
# 但是失敗了，因為「限定長度>=2」的subarray，所以要改用 dict 對應index
class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        N = len(nums)
        if N<2: return False # subarray長度為2以上
        #prefixSet = set([0]) # 是否有重覆出現的
        prefixDict = {}
        prefixDict[0] = -1
        prefixMod = [0]*(N+1) # 存 prefixSum 對k的餘數

        for i in range(N):
            now = (prefixMod[i] + nums[i])%k
            #if now in prefixSet: # 有重覆的餘數
            if now in prefixDict and prefixDict[now]<i-1:
                return True # 表示相減是 k 的倍數，成功了
            #prefixSet.add(prefixMod[i+1]) # 把它加進去set
            if now not in prefixDict: # 沒出現的話，才加
                prefixDict[now] = i # 才能量到最長的距離
            prefixMod[i+1] = now

        print(prefixMod)
        print(prefixDict)
        return False
# case 86/99: [23,2,4,6,6] 7 有重覆的 0 卻沒發現
# case 87/99: [0] 1 只有1個數，但題目希望長度2以上
# case 91/99: [1,0] 2 也是判斷錯誤
# case 82/99: [5,0,0,0] 3
