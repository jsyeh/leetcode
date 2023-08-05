# //思考：有這麼多數字，要如何比對呢？可能要用 DP 吧 （用模擬題的話，會不會超時？因為nums.length<=100000
# //最差的情況，每個數字都不同。那要 100000 次。或許用 HashMap 可以知道數字出現幾次
# //這題可能用 Python 會很方便，因為list剛好是circular list, 頭尾直接相鄰，且 HashMap 可用 dict {}
# 要挑哪一個數呢？或許可以倒過來，用感染的想法來做，看模擬的結果如何 (也就是需要 dist 的 sort 功能)
# 最大的距離，可能就是關鍵：找最大的距離，但不能用暴力法找最大的距離
# 最後一個人的距離不準，因為它沒考慮 circular的狀況 （可以用反過來的迴圈來計算）但沒關係，因為是真的距離
# 第一個人的距離也不準，因為它沒有前一個人的資訊
class Solution:
    def minimumSeconds(self, nums: List[int]) -> int:
        N = len(nums)
        history = [-1]*N  # history distance
        prevPos = {}
        maxDist = {}
        for i in range(N):
            now = nums[i]
            if now in prevPos:
                prevP = prevPos.get(now) # 之前出現過的位置
                dist = i - prevP # 之後要處理 circular 的狀況
                prevDist = maxDist.get(now)

                if prevDist == -1:
                    maxDist[now] = dist # 第一次放入距離
                elif dist>prevDist:
                    maxDist[now] = dist # 更新新的距離，表示最大的距離哦！！！
                prevPos[now] = i # 更新新的位置
                history[i] = dist # debug 用，看距離是多少 # history distance
            else:
                maxDist[now] = -1
                prevPos[now] = i
                history[i] = -1 # history distance
#        print(nums)
#        print(history)
        # 再做一次迴圈，便能找到正確的 max distance 值
        for i in range(N):
            now = nums[i]
            if now in prevPos:
                prevP = prevPos.get(now)
                dist = i + N - prevP
                prevDist = maxDist.get(now)
                
                if history[i] == -1:
                #if prevDist == -1:
                    history[i] = dist
                    if dist>prevDist:
                        maxDist[now] = dist
                #elif dist>prevDist: #有值的，就不要再更新了
                #    maxDist[now] = dist
                prevPos[now] = i
            # else 應該不會有 else 了
                
#        print(history)
        ans = 999999 # 最大的距離 (想找到最小的最大距離)
        for key in nums: # 每個key都去找它的最大距離，希望在當中找到最小的值，因為它就是答案的線索
            d = maxDist[key]
#            print(key, d)
            if d<ans: ans = d
#        print(maxDist)
#        print("====")
                
        if ans%2==0: return int(ans/2)
        else: return int(ans/2)
