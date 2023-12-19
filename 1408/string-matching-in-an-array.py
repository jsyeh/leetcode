# 把所有的 substring 找出來。所以用暴力全試即可
class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        ans = set()
        for w1 in words:
            for w2 in words:
                if w1==w2: continue # 因每個字都不同，相同就是遇到自己，跳掉
                if w1.find(w2)!=-1: # w1 裡面有找到w2的話
                    print(w1,w2)
                    #ans.append(w2) # w2就是 substring
                    ans.add(w2)
        return list(ans) # 轉成 list
# case 6/67: ["leetcoder","leetcode","od","hamlet","am"]
# 我找到重覆的 "od" "od" 這不合理哦！因為有用過了！
# 因此，應該用 set() 來放，再轉成 list
