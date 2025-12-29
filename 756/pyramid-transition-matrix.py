# LeetCode 756. Pyramid Transition Matrix
# 有 allowed 的很多「小三角堆」，要在 bottom 的基礎上，堆出「金字塔」
class Solution:
    def pyramidTransition(self, bottom: str, allowed: List[str]) -> bool:
        table = defaultdict(list)  # 先建立「底座」對照表
        for a, b, c in allowed:  # 小金字塔的「底座」是 a+b ，上層是 c
            table[a+b].append(c)  # 底座是 a+b，將能查表、找到上層是 c
            
        def helper(base, i, upper):  # 用「函式呼叫函式」照著 base 建 upper 
            if len(base)==1:  # 終止條件：到達金字塔頂端
                return True  # 成功建出「最上面的尖頂」太棒了！
            if i>=len(base)-1:  # 到右邊界，可嘗試「往上」升一層
                return helper(upper, 0, '')  # 「函式呼叫函式」以upper當base

            for c in table[base[i]+base[i+1]]:  # 還在同一層，有哪些可能的「上層」
                if helper(base, i+1, upper+c):  # 函式呼叫函式「往右」建「上層」
                    return True  # 只要任一個小分支「成功」，就能建出「金字塔」
            return False  # 都沒有成功的話，這個 helper() 分支「失敗」
            
        return helper(bottom, 0, '')  # 函式呼叫函式，從底層開始「往右」建「上層」
