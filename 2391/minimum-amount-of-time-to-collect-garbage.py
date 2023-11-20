# 很生活化、簡化的題目，要回收金屬M、紙類P、玻璃G的回收物
# 卡車移動需 travel[i] 時間，每台卡車只裝1種回收物（每個花1分鐘）
# 問「全部收完」需多久時間。看來很簡單，就照著迴圈收集即可
# 如果車沒用到，就扣掉（最後一站）後面的時間即可。
# 或著說：車最後一次用到的時間 lastTime[c] 加起來 + 收幾個回收物
class Solution:
    def garbageCollection(self, garbage: List[str], travel: List[int]) -> int:
        N = len(garbage) # 次數的地點數，給迴圈使用
        ans = 0 # 目前花費的時間
        elapsedT = 0 # 卡車從[0]到某一站[i]行駛經過的時間
        lastTime = {'M':0, 'P':0, 'G':0} # 最後累積行駛的時間
        for i in range(N):
            for c in garbage[i]: # 針對每個字母來回收
                lastTime[c] = elapsedT # 某卡車要累積走到這裡
                ans += 1 # 回收1個回收物，花1分鐘
            if i < N-1: # 最後1筆不加，所以有卡判斷
                elapsedT += travel[i] # 到下一站時，累積行駛時間
        for k in lastTime: # 再看（每台）卡車「開了多遠」
            ans += lastTime[k] # 把開車的時間加起來
        return ans
        
