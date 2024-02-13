# encoded[i] = arr[i] XOR arr[i+1]
# 所以 arr[i+1] = arr[i] XOR encoded[i]
class Solution:
    def decode(self, encoded: List[int], first: int) -> List[int]:
        ans = [first] # 先擺好 first
        for i in range(len(encoded)): # 再逐一處理
            # arr[i+1] = arr[i] XOR encoded[i]
            ans.append(ans[-1]^encoded[i]) 
        return ans
