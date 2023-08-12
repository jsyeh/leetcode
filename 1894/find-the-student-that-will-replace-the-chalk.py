# 有點像模擬題，k -= chalk[i] 但是 k<=10^9太大了，要算很久。
# 可以先取餘數後，用 binary search找答案
class Solution:
    def chalkReplacer(self, chalk: List[int], k: int) -> int:
        N = len(chalk)
        all = sum(chalk)
        k = k % all # 這樣可以直接針對最後一輪，直球對決

        for i in range(1,N): # 把 chalk[i] 改成 sunning sum
            chalk[i] += chalk[i-1] # running sum

        left, right = 0, N # 右不包含

        while left < right:
            mid = (left+right) // 2
            if chalk[mid] == k: 
                return (mid+1)%N # 找到答案嗎？其實是「下個人」要去補粉筆
            if chalk[mid] < k: # 粉筆夠用
                left = mid + 1
            else:
                right = mid
        return left
# case 71/72: 有一大堆1
# 這個故事說明：剛好把 chalk 用完的人，其實是「下一個人」才要去補粉筆
