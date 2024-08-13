# LeetCode 40. Combination Sum II
# 希望加起來是 target，把「所有可能的組合」回傳
# 可用 DFS 暴力找可能的答案。過程中有 nowList 存下現況
class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()  # 小到大，排序好，以便「相同數字」相鄰（若有跳過的數，之後也跳過）
        N = len(candidates)
        ans = []  # 一開始「答案」是空的
        nowList = []  # 用 nowList 存下現況
        def dfs(nowSum, nowI, prevSkip): # 用暴力 DFS 找答案（若有跳過的數，之後也跳過它）
            if nowSum == target:  # 若找到答案
                ans.append(nowList[:]) # 使用 [:] 複製一份，再塞入「答案」裡
                return  # 找到答案，就「不再繼續」增長
            if nowSum > target:  # 若超過
                return  # 超過，就「不再繼續」嘗試
            if nowI < N:  # 如果還在合理範圍（還有數字能嘗試）
                # 可以跳過「現在這個數」
                dfs(nowSum, nowI+1, candidates[nowI]) # 決定跳過「現在這個數」，函式呼叫函式
                # 也可不跳過「現在這個數」
                if prevSkip!=candidates[nowI]:  # 要小心「之前若跳過此數」同樣的數就不再用
                    nowList.append(candidates[nowI]) # 先推入 nowList
                    dfs(nowSum+candidates[nowI], nowI+1, prevSkip) # 函式呼叫函式
                    nowList.pop() # 再吐出 nowList
                
        dfs(0, 0, -1)  # 一開始nowSum=0, 將處理 nowI=0，前個跳掉的數prevSkip=-1 沒有
        return ans  # 最後的「答案」
