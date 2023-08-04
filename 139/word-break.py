# 解題策略：先將 wordDict 建出 HashSet 以便查表
# 接下來，暴力拆字，找「所有能到的位置」。最後看能不能拆到最後的字母
import queue
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        hashSet = set()
        maxWordLen = 0
        for word in wordDict:
            hashSet.add(word)
            a = len(word)
            if len(word) > maxWordLen:
                maxWordLen = len(word)
        
        N = len(s)
        visited = [False]*(N+1)
        q = queue.Queue()
        q.put(0) # 從0開始走
        visited[0] = True

        while q.qsize() > 0:
            left = q.get() # 現在要處理的位置
            for dist in range (1,maxWordLen+1): 
                # 可能的字串長度。但不能叫len因為len()衝突
                if left+dist>N: continue
                if visited[left+dist]: continue # 走過，不用再走
                if s[left:left+dist] in hashSet:
                    if left+dist==N: return True
                    q.put(left+dist)
                    visited[left+dist] = True

        return False # 前面沒有 return True 的話，表示走不到最後，那就False
