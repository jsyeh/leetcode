class Solution {
public:
    int rangeBitwiseAnd(int left, int right) {
        int shift=0;
        while(left!=right){
            left = left>>1;
            right = right>>1;
            shift++;
        }
        return left<<shift;
    }
};//因為數字很大，絕對不能用for迴圈逐項去AND
//可能可以用分類的方法來測，也就是32 bits 都去試
//AND要留下來的難度很高，很容易變成0
//最後是看解說，使用Algorithm 1
