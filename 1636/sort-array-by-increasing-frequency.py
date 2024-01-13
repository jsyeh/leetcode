# 有很多數字，出現的頻率不同。依照頻率來排序。頻率相同時，從大到小排。
# 因數字<=100, 頻率也<=100，所以key可以
class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        counter = Counter(nums) # 統計出現的次數
        # https://stackoverflow.com/questions/20950650/how-to-sort-counter-by-value-python
        #s = reversed(counter.most_common()) # reversed()反過來
        # .most_common() 會依字典的頻率(key,value)，由多到少排好
        # 不過上面的作法有問題，所以改用下面的 .sort()
        s = counter.most_common() # 會依字典頻率(key,value)多到少
        # 不過頻率相同時，要先大數、再小數，所以要有特別的 sort函式
        s.sort(key=lambda x:x[1]*200+100-x[0]) # 奇怪的公式
        # 因為 -100<=nums[i]<=100，加上200個數，所以用上面公式當key
        ans = []
        for k,v in s: # (key,value)
            for i in range(v): # 重覆 v 次
                ans.append(k) # 把 k 重覆 v 次
        return ans
# case 61/180: [1,5,0,5]
