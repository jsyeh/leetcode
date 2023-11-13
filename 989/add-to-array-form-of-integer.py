# 這題是把 10^4 位數的陣列，與10000以下的整數相加
class Solution:
    def addToArrayForm(self, num: List[int], k: int) -> List[int]:
        num.reverse() # 為了迴圈簡單，我把陣列反過來
        # print(num) # Debug 用
        carry = 0 # 進位用
        for i in range(len(num)): # 以陣列為主，進行加法
            num[i] += k%10 + carry # 剝皮法，處理 k
            carry = num[i]//10 # 算出進位的部分
            num[i] %= 10 # 留在原位的部分
            k //= 10 # 剝皮法，處理k
            # print(num) # Debug 用
        # print('second', num, k, carry) # Debug 用
        while k>0 or carry>0: # 如果還有進位 or k 還沒剝完
            now =  k%10 + carry # 繼續剝皮法，處理 k
            carry = now//10 # 算出進位的部分
            k //= 10 # 剝皮法，處理 k
            num.append(now%10) # 因陣列用完了，再插入高位部分
        num.reverse() # 再反回高位到低位的答案形式
        return num
