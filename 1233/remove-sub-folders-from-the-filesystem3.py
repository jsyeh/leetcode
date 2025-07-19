# LeetCode 1233. Remove Sub-Folders from the Filesystem
# 給一堆目錄，把所有 sub-folder 子目錄 都刪掉，只留下「母目錄」
# 可先把 folder 排序，「母目錄」就會先出現(在前面)，後面會接著出現子目錄(要刪掉)
class Solution:
    def removeSubfolders(self, folder: List[str]) -> List[str]:
        folder.sort()  # 先排序，讓「母目錄」在「子目錄」前面
        folderSet = set()  # 曾經出現的目錄，「母目錄」一定在裡面
        for now in folder:
            # 要怎麼「比較字串」比較有效率呢？
            a = now.split('/')  # 把「現在now」的字串，斷成許多「小目錄名」
            bad = False
            for i in range(len(a)):  # 慢慢增加「目錄」的長度，看「母目錄」有沒有出現過
                if '/'.join(a[:i+1]) in folderSet:
                    bad = True  # 有任一個「母目錄」存在，就失敗
            if not bad:  # 沒有失敗
                folderSet.add(now)  # 就加到答案裡
        return list(folderSet)  # 把答案變成 list
