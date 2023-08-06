# 可能的 playlist 數量：總共n首歌，有其他k首歌播放後才能再重覆。目標是湊goal首歌
# table[goal+1][n+1] 的 table[g][j] 要湊g首的歌單,使用j首不同的歌
# 因為答案的可能性太多了，所以要 %10^9+7 即 %1000000007
class Solution:
    def numMusicPlaylists(self, n: int, goal: int, k: int) -> int:
        table = [[0]*(n+1) for _ in range(goal+1)]
        # table[goal+1][n+1] table[g][j]: 要湊g首的歌單,使用j首不同的歌

        table[0][0] = 1 # 最基礎的1種方法：都不放歌

        for g in range(1,goal+1): # 歌單要湊g首歌
            for j in range(1,n+1): # 使用j首不同的歌
                # 狀況1: 前之使用(j-1)首，下一首歌的選擇是未用過的 n-(j-1)
                table[g][j] = table[g-1][j-1] * (n-j+1) % 1000000007
                # 狀況2: 如果有已有的歌單夠長,不同首的歌j > k 的話，
                # k other songs have been played 要隔k首歌、前面k首不同的歌不能用
                # 但是更前面的 (j-k)首歌可重覆使用
                if j > k:
                    table[g][j] += table[g-1][j]*(j-k)
                    table[g][j] %= 1000000007
        return table[goal][n]

