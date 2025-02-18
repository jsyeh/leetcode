# LeetCode 2375. Construct Smallest Number From DI String
# 字母I是Inc增加，D是Dec減少。每位數就「照著」增加 or 減少（可增減任意數量）
# 且「每個數字」只能用一次。找出增減「合規則」的「最小的數」
class Solution:
    def smallestNumber(self, pattern: str) -> str:
        N = len(pattern)
        ans = [0] * (N+1)  # 上下起伏 N 次，就有 N+1 格
        used = set()  # 可用 set() 來記錄 used 的數字
        def dfs(i):  # 使用「函式呼叫函式」的 DFS 來試各種可能
            if i==N: return True  # 順利走到最後
            for now in range(1,10):  # 1到9，每種數字「都試一輪」
                if now in used: continue  # 用過的數字 不能用
                if i==-1 or (pattern[i]=='I' and now>ans[i]) or (pattern[i]=='D' and now<ans[i]):
                    # now 合理的3種狀況：還沒放數字 or 數字增加 or 數字減少
                    ans[i+1] = now  # 就可以先把 now 放在這一格
                    used.add(now)  # 先標記成「用過」
                    if dfs(i+1):  # 使用「函式呼叫函式」的 DFS 來試各種可能
                        return True  # 如果成功，就可以「不用再試」，因為 ans 裡已放滿答案
                    used.remove(now)  # 沒成功的話，再「還原」
            return False
        dfs(-1)  # 從最前面，開始「逐位」測試，直到成功
        return ''.join(list(map(str, ans)))  # 把全部的數字，轉成字母後，接起來

        # （看錯題目）第二次想到的方法，結果漏看「每數只能用1次」
        def dfs(i):
            if i==N: return True  # 順利走到最後
            for now in range(1,10):
                if pattern[i]=='I' and now>ans[i]:
                    ans[i+1] = now
                    if dfs(i+1): return True
                if pattern[i]=='D' and now<ans[i]:
                    ans[i+1] = now
                    if dfs(i+1): return True
            return False
        for now in range(1,10):
            ans[0] = now
            if dfs(0): return ''.join(list(map(str, ans)))
        # （看錯題目）第一個想到的方法，以為只要 +1 or -1
        counter = Counter(pattern)
        diff = counter['D'] - counter['I']
        start = max(diff, 0)
        ans = [start+1]
        for c in pattern:
            if c=='I':
                ans.append(ans[-1]+1)
            else:
                ans.append(ans[-1]-1)
        return ''.join(list(map(str, ans)))

