# 把所有的 sub-folder 子目錄 都刪掉
# 我想到，可以先把 folder 排序，母目錄就會在前面
# 接下來依序將目錄放入 dict 裡
class Solution:
    def removeSubfolders(self, folder: List[str]) -> List[str]:
        s = set() # 用來快速找「現有的母目錄」
        ans = []
        folder.sort() # 排序後，母目錄一定在前面
        for f in folder:
            ff = f.split('/') # 很多目錄的名字，最前面是空
            path = '' # 目錄會慢慢增加
            exist = False
            for i in range(1,len(ff)-1): 
                # 避開 前面空字串 與 後面本身
                path += '/' + ff[i]
                if path in s: # 要刪了
                    exist = True # 所以標示它存在
                    break
            if exist: continue # 避開，換下一筆
            s.add(f) # 留下來
            ans.append(f)# 留下來
        return ans
