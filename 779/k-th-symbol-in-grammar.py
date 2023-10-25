# 這題看起來是「利用0變01、1變10」的文法，產生「越來越長」的數字
# 0 
# 01  
# 01 10 
# 0110 1001
# 接著問第n行的第k個數字。不能用暴力生成法，因k<2^30-1 1024*1024*1024太大
# 所以應該要找到規則。如果用回溯法，了解「是哪個數字」「怎麼產生的」應就解決了
# 可用「函式呼叫函式」的helper()來解決，但要小心 1-index 從1開始數
# 所以在推理時，先把k變成 0-index就會簡單了
class Solution:
    def kthGrammar(self, n: int, k: int) -> int:
        def helper(n, k)->int: # 這裡的 k 改成 0-index
            if n==1: return 0

            if k%2==0: # 偶數，是左邊那個數 (因helper 已改成 0-index)
                prev = helper(n-1, k//2) # 變成「問上一層的問題」
                if prev==0: return 0 # 再依上一層的結果，推這一層的答案
                else: return 1
            else: # 右邊那個數
                prev = helper(n-1, k//2)
                if prev==0: return 1
                else: return 0

        return helper(n, k-1) # 這裡的 k 改成 0-index
# case 39/55: 3 1
