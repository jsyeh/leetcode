# 有套命名規則：挑2個ideas[i] ideas[j], 把第1個字母交換，
# 若「新名字」都沒出現過，就把2字接起來、空格放中間。
# 問「總共有幾個不同的新名字」
# 因為字有 5*10^4 很多字，所以無法暴力挑。
# 可「照著第1個字母」分類，便能照著26字母類，算「排列組合」
class Solution:
    def distinctNames(self, ideas: List[str]) -> int:
        # 先照 26 個字母，建出 字典，對應字母的集合
        lower = 'abcdefghijklmnopqrstuvwxyz'
        table = {c:set() for c in lower}
        # 接著，將字放到對應的類別中的set
        for idea in ideas: # 比如 table['c'] 有含有 offee
            table[idea[0]].add(idea[1:])
        # 再來，看看 table[c] 
        ans = 0
        for c in lower: # 小寫字母的26類，互相比較
            for c2 in lower: # 另外的26類
                if c == c2: continue # 避開相同的部分
                total = len(table[c] & table[c2]) # 全部
                ans += (total-len(table[c2])) * (total-len(table[c]))
                # 排列組合: 左邊能用的 * 右邊能用的 
        return ans
