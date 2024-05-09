# 小朋友很開心，要挑小朋友。不過挑了一位小朋友後，其他沒被挑到的小朋友就漸漸不開心了
# 一次只能挑一位，要請問怎麼挑，可以得到最高的「快樂分數」
# 其實照著排序，再依序從高到低挑，就可以知道答案了，快樂值降到0就停下來。簡單。
# 只是在挑的時候，有 2*10^5 個人要挑，數量有點多，要能提早離開迴圈。
# 另外如果要挑的人比較少，不用 sort 而改用 priority queue 會更快。
class Solution:
    def maximumHappinessSum(self, happiness: List[int], k: int) -> int:
        happiness.sort(reverse=True)
        ans = 0
        for i in range(k):
            if happiness[i]>i:
                ans += happiness[i] - i
            else:
                break
        return ans
