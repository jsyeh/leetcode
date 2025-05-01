# LeetCode 2071. Maximum Number of Tasks You Can Assign
# 可用 binary search 去找「答案」（能做幾個工作）
# 而 helper()函式裡，又用了 binary search 去挑「最適合吃藥丸」的人
class Solution:
    def maxTaskAssign(self, tasks: List[int], workers: List[int], pills: int, strength: int) -> int:
        W, T = len(workers), len(tasks)
        tasks.sort()  # 簡單的工作，排在前面（前k項，會從右邊往左邊取）
        workers.sort()  # 越後面的人，能力越強（會從右邊往左邊取）
        def helper(k):  # 請問答案「不夠完成 k 個工作嗎？」（是否「做不到」）
            if k>W: return True  # 人數不夠，是的「做不到」
            p = pills  # 現在有幾個藥丸能用
            w = workers[:]  # 複製陣列，用完就從右邊刪掉
            for i in range(k-1, -1, -1):  # 「前k項簡易」的工作
                # 把「前k項簡易」的工作，「從難到易」依序處理
                if w[-1]>=tasks[i]:  # 能力最強的，能解最難問題，直接接案
                    w.pop()  # 接案後，離開去工作，陣列變小了（少了1人）
                elif p>0:  # 不能直接接案/不夠力、但還有藥丸時，挑最適合的人吃藥
                    theone = bisect_left(w, tasks[i]-strength)  # 吃藥後，最適合的人
                    if theone >= len(w): return True  # 最強的人，吃藥後還是不行，「是的，做不到」
                    w.pop(theone)  # 接案後，離開去工作，陣列變小了（少了1人）
                    p -= 1  # 用掉1顆神奇的藥丸
                else:  # 都不行，就失敗
                    return True  # 「是的，做不到」
            return False  # 哈哈，做得到哦！不是「做不到」 （這樣寫，可讓bisect_left()運作順利）
        return bisect_left(range(1,min(W,T)+1), True, key=helper)
