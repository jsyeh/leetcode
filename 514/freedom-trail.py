# 轉盤ring上有許多字母，想要左右轉動，組出 key 字串（密碼鎖解鎖）
# 需要轉、需要按。問要做幾個動作，才能全部完成 key。
# 因 ring 裡，可能有重覆的字母，所以轉動的方法不只一種。
# 希望轉動的格子數要少，而前面轉的位置，會影響後面轉的距離。
# 因為「左轉、右轉」100個字，需要2^100次方，不能用暴力法（太久）。
# 看起來像 DP 的題目，但有點難寫。
# 在 Solutions 裡，shawngao提出了簡單易理解的方法，就是3層迴圈，
# 利用 buttom up DP ，m-1...0 去更新 table[i][j] 的值。
# lee215提出改進，只針對 key[k] 字母對應的位置做分析，能讓迴圈的範圍變更小。
class Solution:
    def findRotateSteps(self, ring: str, key: str) -> int:
        R = len(ring)
        pos = collections.defaultdict(list)  # 字母的位置對照表
        for i, c in enumerate(ring):  # 建出字母對照表，看字母在「轉盤」的哪裡
            pos[c].append(i)  # 記錄對應的位置。因同個字母「可能有多個位置」故用list

        state = {0: 0}  # 目前可能的 state：第0步，在位置0，累積轉動付出的代價是0
        for c in key:  # 逐個字母處理，慢慢達成
            next_state = {}  # 為了字母c在位置 p 要付出的代價(下次要用)
            for p in pos[c]:  # 這個字母c「有哪些可能的位置」possible position
                next_state[p] = inf  # 先設「無限大」，稍後會更新
                for prev in state:  # 之前的（可能）位置
                    # 「前一個位置 prev」 到「現在可行的目標位置 p」 要走幾步
                    diff = min(abs(p - prev), R - abs(p - prev))  # 挑1個方向轉diff格
                    next_state[p] = min(next_state[p], diff + state[prev])  # 更新「代價」
            state = next_state  # 接力，下次迴圈，從這裡出發
        return min(state.values()) + len(key)
        # 付出的代價 = 走到最後的「移動步驟」 + 按下 len(key)次「確認鍵」
# case 18/303: ring="abcde" key="ade"
