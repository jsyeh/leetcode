# 希望「每個字母」出現次數相同
class Solution:
    def equalFrequency(self, word: str) -> bool:
        counter = Counter(word) # 利用 Counter() 統計字母出現次數
        # 將出現次數 先變成 list 再排序，以便比較
        freq = sorted(list(counter.values()))
        # print(freq)

        # 只有1種字母的話，一定True
        if len(freq)==1: return True

        # 如果最多的數剛好是1個的話，也是成功，因為扣掉就沒差
        if freq[-1]==1: return True

        # 如果最少的那個剛好是1 and 其他都相同的話，也行
        if freq[0]==1 and freq[1]==freq[-1]: return True

        # 2個以上字母的話，希望最多的 freq[-1] 剛好多1個
        # 即剛好比最少的 freq[0] 或 freq[-2]都多1個
        if freq[0]+1==freq[-1] and freq[-2]+1==freq[-1]: return True
        return False
# case 38/50: "bac"
# case 44/50: "abbcc"
