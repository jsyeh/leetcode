# 題意：把 target 拆成 多個字串 串接起來，字串由 source 刪減而來
# 可能可以用 HashSet, 也就是 Python 的 set 來看字串有無存在
class Solution:
    def shortestWay(self, source: str, target: str) -> int:
        # 先測試「有沒有缺字母」
        source_set = set(source)
        for c in target:
            if c not in source_set: # 應會比 if c not in source 快
                return -1 # 提早結束

        # 我有先試暴力法：把source的字全部斷開，再於target做類似的比較
        # 但 Editorial 說，這不可行
        # 所以改用 Solutions 裡最多人按讚的 happyleetcode 的greedy解法1
        # https://leetcode.com/problems/shortest-way-to-form-string/solutions/330938/happyleetcode
        s = 0 # index for source
        t = 0 # index for target
        ans = 1 # 用了幾次substring字（保證有解，因為最差就一堆字組起來
        while t < len(target): # 慢慢將 target[t] 組起來
            while s<len(source) and source[s] != target[t]:
                s += 1 # 若 source[s]不能用，換下一格
            if s==len(source): # 如果source[s]走到䀆頭，要結束這回合
                s = 0 # 重新在 source 裡找，即 source[0]重新開始
                ans += 1 # 新的開始，要再增加1個字
                continue
            s += 1 # 若有幸走到這裡，表示有找到對應的字母，太好了
            t += 1 # 就讓 s 和 t 都走到下一格
            # 這種 greedy 的解法，可儘量讓substring長度長一點，ans就最小
        return ans

