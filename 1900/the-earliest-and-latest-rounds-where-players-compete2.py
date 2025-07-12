# LeetCode 1900. The Earliest and Latest Rounds Where Players Compete
# n 個人(1...n)對決，從 round 1 開始「頭尾2人」逐組對決、淘汰 n//2 人，中間若只有1人「直接晉級」。
# 每個 round 比完，晉級者照原本順序站好，再「頭尾2人」逐組對決，直到「第1名、第2名」相遇就結束。
# 「第1名、第2名」一定會贏其他人，其他「你來決定勝負」。最快、最慢「第幾個round」2人會相遇、結束比賽？
class Solution:
    def earliestAndLatest(self, n: int, firstPlayer: int, secondPlayer: int) -> List[int]:
        @cache  # 我參考 Dmitry 解法，「函式呼叫函式」用「左邊數第幾個、右邊數第幾個」的「規律」來簡化
        def helper(left, right, n, rounds):  # 左邊數、右邊數、共幾人、第幾次round
            if left==right:  # 左邊數、右邊數「距離相等」兩人撞在一起，比賽結束
                ans.add(rounds)  # 比賽結束時，記錄「比賽了幾個rounds」（用set()避開重覆的答案）
                return  # 提早結束
            # 因對稱結果相同，為簡化問題，希望左邊數「較小」、右邊數「較大」
            if left > right:  # 但大小不對，想鏡射成「左右對稱的問題」
                left, right = right, left  # 可交換參數
            # 下面迴圈是「精華」，把所有可能「都試過一次」
            for i in range(1, left+1):  # 下一輪「第1名選手」左邊數，排第幾個
                # i-1 對應第1名選手的「左邊有幾位晉級」，那右邊在 left<right 的範圍內，要少 (i-1)人
                for j in range(left-(i-1), right-(i-1)):  # 下一輪「第2名選手」右邊數，排第幾個
                    if (n+1)//2 < i + j: continue  # 下一輪人數，不夠放「左i,右j」（淘汰過頭）
                    if i + j < left+right-n//2: continue  # 避開「左i,右j」太小、外面全淘汰也不夠
                    helper(i, j, (n+1)//2, rounds+1)  # 淘汰 n//2 人，下一輪比賽剩 (n+1)//2 人
        ans = set()  # 記錄「比賽幾個rounds」後結束
        helper(firstPlayer, n-secondPlayer+1, n, 1)  # 左邊數、右邊數、共n人、第1次round
        return [min(ans), max(ans)]  # 最少round數、最大round數 
