# 要找到 [left, right] 的字串，使得 int(s[left:right+1]) ^ first == second
# 因為 XOR 有交換律，所以其實 int(s[left:right+1]) == second ^ first
# 不過有另外的問題，在 case 55/59 測資太長太長了， s.find()會很沒有效率而超時。
# 那能不能「不要用字串比對」而用 整數的因數之類的解法呢？
# 偷看 lee215 和 votrubac 的解法，都會使用 hashmap 來解
# 我想，應該是先分析 s 字串裡，不同 (left,right) 對應的字串都放到 hashmap 裡
# 之後查 binary 字串有沒有出現過，有的話直接把之前存的 (left,right) 拿來用
# 但 10^4 * 10^4 會超時，但因 int 只有 32 bit 且題目說 <= 10^9 約 10*3＝30 bit
# right 最多是 left + 30 這樣就不會超時了
class Solution:
    def substringXorQueries(self, s: str, queries: List[List[int]]) -> List[List[int]]:
        # 將 s 字串裡，最長 30 的全部子字串，都建立 hashmap
        table = {} # table[子字串對應的整數] = {left,right}
        N = len(s)
        for i,c in enumerate(s): # 左邊界
            if c=='0':
                continue # 因為0開頭的字不合理，所以跳掉
            for right in range(i+1,min(N, i+30)+1): # 右邊界
                val = int(s[i:right],2)
                if val not in table:
                    table[val] = [i,right-1]
        zero = s.find('0') # 但是第1次出現的0會很重要，事先要加入字典
        table[0] = [zero, zero] # 找不到的話 [-1,-1]也是答案
        # print(table)
        ans = []
        for query in queries:
            first, second = query
            val = first ^ second
            if val in table:
                ans.append(table[val])
            else:
                ans.append([-1,-1])
        return ans
        """ # 下面是會 Time Limit Exceeded 超時的方法，放棄
        ans = []
        for first, second in queries:
            # print(first, second)
            val = first ^ second # 照前面的發現，算出 val 的值
            #print('val', val)
            '''
            # 可能我的 convertBin() 很沒有效率。改用 str(bin(val))
            def convertBin(val): # 把 val 轉成2進位，使用剝皮法
                if val == 0: return '0' # 特別處理 0 的部分，因它無法剝皮
                ans = ''
                while val>0:
                    ans = str(val%2) + ans
                    val = val // 2
                return ans
            now = convertBin(val)
            '''
            now = str(bin(val))
            #print('now',now)
            left = s.find(now) # 看能不能找到字串
            if left != -1:
                ans.append([left, left+len(now)-1 ]) # 因右包含，所以-1
            else:
                ans.append([-1, -1])
        return ans
        """
# case 5/59: "111010110"
# [[4,2],[3,3],[6,4],[9,9],[10,28],[0,470],[5,83],[10,28],[8,15],[6,464],[0,3],[5,8],[7,7],[8,8],[6,208],[9,15],[2,2],[9,95]]
# 也就是遇到 val = 0 的時候，我的答案會出錯。
# case 55/59: 超長的測資，會超時。可能是我的程式沒有效率。
