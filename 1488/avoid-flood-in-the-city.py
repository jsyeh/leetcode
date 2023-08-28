# 什麼時候會做洪水flood呢？ 任何一個湖「如果有水在裡面」且又下在同一個湖，就會有洪水
# 每天的雨「會下在 rain[i] 的地方」
# [1,2,3,4] 表示下雨會分別將 [1,2,3,4] 個湖都弄滿，沒有任何一個湖下兩次，很好
#   而它對應的答案是 [-1,-1,-1,-1] 表示「因為都在下雨」，所以都沒有瀉洪
# [1,2,0,0,2,1] 表示先下1，再下2，接著兩天可將1，2弄乾。再下2，再下1，平安沒事
#   答案 [-1,-1,2,1,-1,-1] 表示「前兩天有下雨」（沒瀉洪）再兩天沒雨，快把2,1瀉洪
#   最後2天又下雨，又不能瀉洪。這套「防洪規劃」成功了，沒有做大水。
# 對了，if you chose to dry an empty lake, nothing changes.
# 策略：記下 zeros, 記下 fulls。有重覆full時，在 zeros找到合適的一天瀉洪
class Solution:
    def avoidFlood(self, rains: List[int]) -> List[int]:
        N = len(rains)
        ans = [-1]*N
        zeros = [] # 有哪些天不下雨，能好好利用
        fulls = {} # HashMap fulls[lake] = date哪天下雨
        for i in range(N): # day i 
            rainLake = rains[i] # day i 下雨在 rainLake 這個湖
            if rainLake==0: # 沒有下雨的話
                zeros.append(i) # 把這一天記起來
                ans[i] = 1
            else:
                if rainLake in fulls: # 不幸將在已滿的 rainLake 下雨
                    # 要在下雨前找一天（沒下雨的） zeros 事先瀉洪
                    if len(zeros)==0:
                        return [] # 沒有空白的晴天日子能用，慘
                    theDay = fulls[rainLake] # 要找 theDay後的zero day
                    left, right = 0, len(zeros)
                    while left<right:
                        mid = (left+right)//2
                        if zeros[mid] < theDay:
                            left = mid + 1
                        else:
                            right = mid
                    # left 是 dry day
                    if left >= len(zeros): return [] # 超過範圍，沒救

                    next = zeros[left] 
                    ans[next] = rainLake
                    # 糟，list要刪掉某格，很花時間
                    zeros.pop(left)
                    fulls[rainLake] = i
                else:
                    fulls[rainLake] = i # 記得是哪一天把 rainLake 塞滿的

        return ans
# case 6/82: [69,0,0,0,69]
# case 8/82: [0,1,1]
# case 78/82: [1,0,2,0,3,0,2,0,0,0,1,2,3]
