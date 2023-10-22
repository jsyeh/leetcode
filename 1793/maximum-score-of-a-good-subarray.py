# 本題想找到（包含 nums[k）的連續陣列的 max good score
# good score 的定義，是連續n個數字，n*min(陣列最小值)
# 它是 Hard 題，一開始沒有頭緒 -- 看了Editorial的解說後，心情很亂，還是沒頭緒
# 但看了 Solutions 裡 leet215的解法，簡單有力。
# 它的Greedy想法，是 i = j = k 再i往左擴展、j往右擴展
# 擴展時，可能會讓 min(陣列最小值)變小，所以要優先往「不會變太小」的那一邊擴展
# 邊擴展時，邊更新 ans 值，就解決了。我的程式沒有很精簡，但應該容易理解
class Solution:
    def maximumScore(self, nums: List[int], k: int) -> int:
        N = len(nums)
        i, j = k, k # i是左邊界，j是右邊界，都包含，所以程式會較簡單
        min_one = nums[k] # nums[i:j+1] 裡面最小的那個數
        ans = min_one * 1 # Maximum Socre of a Good Subarray，目前只看到1個數
        while i>0 or j<N-1: # 左右只要還有人沒超過範圍
            while i>0 and nums[i-1]>=min_one: # 只要能簡單往左擴展
                i -= 1 # 就持續往左擴展
                ans = max(ans, min_one*(j-i+1)) # 並更新ans
            while j<N-1 and nums[j+1]>=min_one: # 只要能簡單往右擴展
                j += 1 # 就持續往右擴展
                ans = max(ans, min_one*(j-i+1)) # 並更新ans
            # 前面2個while迴圈，能先往左右持續擴展。
            # 直到卡住時，由下面決定要「如何挑選」會變小的數
            if i>0 and j<N-1: # 兩個邊界都還能擴展
                if nums[i-1]>nums[j+1]: # 左邊大，應往左邊擴展
                    i -= 1
                    min_one = min(min_one, nums[i])
                    ans = max(ans, min_one*(j-i+1))
                else: # 右邊大，應往右邊擴展
                    j += 1
                    min_one = min(min_one, nums[j])
                    ans = max(ans, min_one*(j-i+1))
            elif i>0: # j走到底了，只能往左邊發展
                i -= 1
                min_one = min(min_one, nums[i])
                ans = max(ans, min_one*(j-i+1))
            elif j<N-1: # i走到底了，只能往右邊發展
                j += 1
                min_one = min(min_one, nums[j])
                ans = max(ans, min_one*(j-i+1))
        return ans
# 雖然我寫得很囉嗦，不過還蠻容易懂的，就照著 lee215 的解法概念
# 如果有了這Greedy概念，這題不難 Median 而已
# 但是如果沒有這個概念，那真的很難想懂，所以這題是 Hard 無誤
