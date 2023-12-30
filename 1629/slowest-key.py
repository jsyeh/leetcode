# 想知道哪個 key 按最久，就依字母統計時間差即可
# 注意，不是「累積按最久」，是「單鍵按最久」
class Solution:
    def slowestKey(self, releaseTimes: List[int], keysPressed: str) -> str:
        N = len(keysPressed)
        ans, ansT = keysPressed[0], releaseTimes[0]
        for i in range(1,N):
            diff = releaseTimes[i] - releaseTimes[i-1]
            if diff>ansT or (diff==ansT and keysPressed[i]>ans):
                ansT = diff
                ans = keysPressed[i]
        return ans
        
        ''' # 下面的寫法誤以為是「累積按最久」所以用字典，沒效率
        N = len(keysPressed)
        d = defaultdict(int)
        for i,c in enumerate(keysPressed):
            if i==0: # 最前面的字母，直接拿值來用
                d[c] = max(d[c], releaseTimes[i])
            else: # 其他字母，就用「時間差」
                d[c] = max(d[c], releaseTimes[i] - releaseTimes[i-1])
        ans = keysPressed[0] # 先隨便挑個字母，當成答案
        for c in d: # 如果時間更長 or 時間相同但字母序大
            if d[c]>d[ans] or (d[c]==d[ans] and c>ans):
                ans = c # 就更新答案
        print(d)
        return ans
        '''
# case 63/109: [1,2] "ba" 時間相同時，要字母序大的
# case 66/109: 超長的，怎麼辦？
