# 在 nums 裡，找「連續的subarray」裡面有一樣多的0和1
# 可想像「爬山」「爬樓梯」，到任一個高度時，往前回顧「之前是否有相同高度」
# 曾有「相同高度」便可往前「拉距離」量測。沒出現過，就記下現在的位置，供之後比距離。
# 去年8月剛學Python時，也有寫過這題，不過當時的程式碼比較亂。
# 現在對Python很熟練，再寫一次，看是否更清楚。
class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        prevPos = {0:-1} # 做出對照表，之前高度0的時間，在-1的位置
        ans = 0
        p = 0 # prefix sum，就是爬山時的高度，會高高低低出現
        diff = [-1,+1] # 往上爬 or 往下爬
        for i,num in enumerate(nums):
            #p += num if num==1 else -1 # 1:+1, 0:-1 上上下下爬
            p += diff[num] # 1:+1, 0:-1 上上下下爬
            if p in prevPos: ans = max(ans, i-prevPos[p]) # 之前出現過，就更新答案
            else: prevPos[p] = i # 沒出現過，就記錄「此高度」對應的位置
        return ans
