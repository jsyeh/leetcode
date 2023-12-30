# 要把 the sum of intervals 都加起來
# 比如說 [2,1,3,1,2,3,3]
#            3 要把 另外2個3與它的index距離加起來
# 不過數字太大時，兩層迴圈要算太久，所以我失敗了！！！！
# 修正： 這些距離的計算，可分成 prefix 及 postfix 兩群
class Solution:
    def getDistances(self, arr: List[int]) -> List[int]:
        N = len(arr)
        prefixIsum = [0]*N
        postfixIsum = [0]*N
        prefixIcount = [0]*N
        postfixIcount = [0]*N

        indexSum = defaultdict(int) # 從左到右（第一輪）
        indexCount = defaultdict(int)
        for i,now in enumerate(arr): # 左到右，統計 prefix
            prefixIsum[i] = indexSum[now]
            prefixIcount[i] = indexCount[now]
            indexSum[now] += i
            indexCount[now] += 1

        indexSum = defaultdict(int) # 從右到左（第二輪）
        indexCount = defaultdict(int)
        for i in range(N-1,-1,-1):
            now = arr[i]
            postfixIsum[i] = indexSum[now]
            postfixIcount[i] = indexCount[now]
            indexSum[now] += i
            indexCount[now] += 1

        # 最後，算出答案 相同 arr[i] 的 index 距離
        ans = []
        for i in range(N):
            leftDist = -prefixIsum[i] + i*prefixIcount[i]
            rightDist = postfixIsum[i] - i*postfixIcount[i]
            ans.append(leftDist+rightDist)
        return ans

        ''' # 以下的方法太慢，上面重寫
        pos = defaultdict(list) # 可知道某個數值n 對應的位置 pos[n]
        for i,now in enumerate(arr): # 第一輪，建表格
            pos[now].append(i) # 記錄 arr[i] 的 i

        ans = []
        for i,now in enumerate(arr): # 第二輪，找答案
            dist = 0
            for ii in pos[now]: # 全部與 now 相同的 index ii
                dist += abs(ii-i) # ii 都去算與 i 的距離
            ans.append(dist)
# 所以我失敗了！！！！
        return ans
        '''
