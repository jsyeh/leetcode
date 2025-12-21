# LeetCode 955. Delete Columns to Make Sorted II
# 希望 strs 裡 strs[0] <= strs[1] ... <= strs[N-1] ex. "aaa" <= "aab" <= "xaa"
# 需整個字串「上面的字串小、下面的字串大」，要刪掉幾個 column? (昨天 944 只比對應「單一」字母)
class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        N = len(strs)  # 有 N 條字串
        ans = 0  # 要刪掉幾個 column 呢？
        already_ok = [False] * (N-1)  # 相鄰 N-1 組字串，是否大小OK
        for j in range(len(strs[0])):  # 左到右，每個 col j 逐一檢查
            old_ok = already_ok[:]  # 備份 already_ok 陣列「舊資料」，失敗時「可還原」
            for i in range(N-1):  # 檢查「相鄰 N-1 組字串」
                if already_ok[i]:  # 左邊曾經成功（上小、下大），右邊就不用再試了
                    continue  # 不用處理，換「下一組i」
                if strs[i][j] > strs[i+1][j]:  # 在 col j 發生「不符合排序」
                    ans += 1  # 要將整個 col j 刪掉，稍早標示的 already_ok[i] 已無效
                    already_ok = old_ok  # 放棄這一輪稍早第19行 already_ok，還原「舊資料」
                    break  # 這一輪 for i in range(N-1) 已失敗，不用再試了
                if strs[i][j] < strs[i+1][j]:  # 現在 col j 開始，明顯字典順序
                    already_ok[i] = True  # 標示「row i 和 row i+1」已OK
        return ans
