# LeetCode 1233. Remove Sub-Folders from the Filesystem
# 給一堆目錄，把所有 sub-folder 子目錄 都刪掉，只留下「母目錄」
# 可先把 folder 排序，「母目錄」就會先出現(在前面)，後面會接著出現子目錄(要刪掉)
class Solution:
    def removeSubfolders(self, folder: List[str]) -> List[str]:
        folder.sort()  # 先把照著子母排序排好

        ans = []  # 「母目錄」會放在這裡
        prev = ''  # 前一層的目錄名(「母目錄」,就不是子目錄)
        for f in folder:
            # 第1個出現的是「母目錄」。如果與前一個母目錄「開頭不同的」是新的母目錄
            if len(ans)==0 or (not f.startswith(ans[-1]+'/')):  
                # ans[-1]+'/'是前次出現的母目錄, f 的開頭若與它不同, 就是新的母目錄
                ans.append(f)
            # print(f)  # 這是 debug 用的, 方便大家觀察結果 (上傳前記得刪掉)
        return ans
        
