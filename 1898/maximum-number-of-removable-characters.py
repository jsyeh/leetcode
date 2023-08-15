# 想知 removabl[i] 最多可刪k個字母，讓 p 還是 s減字母 的 subseq
# 就可用 binary search 找到 k 是多少
class Solution:
    def maximumRemovals(self, s: str, p: str, removable: List[int]) -> int:
        S, P, R = len(s), len(p), len(removable)
        def remove(k: int) -> bool: # 刪除前k個字，p是否還是subsequence
            removed = set()
            for i in range(k): # 先將前k個index放到removed set裡
                removed.add(removable[i])

            i2 = 0
            for i in range(S): # 逐個字母檢查
                if i not in removed: # 如果沒有被刪掉
                    if p[i2]==s[i]:
                        i2 += 1
                        if i2 >= P: return True # 成功比對到字串p最後字母
            return False # 沒將 p 都比對完，就失敗了

        left, right = 0, R+1 # R+1 讓 R 可以用到底
        while left<right:
            mid = (left+right) // 2
            if remove(mid):
                left = mid + 1
            else:
                right = mid

        return left -1
# case 56/67: "qlevcvgzfpryiqlwy" "qlecfqlw" [12,5] 因 R 用到底
