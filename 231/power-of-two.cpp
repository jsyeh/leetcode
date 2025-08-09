// LeetCode 231. Power of Two
// 題目給你數字 n 請回答 return True 還是 return False
// 如果它是 2的很多次方 True  ex. 1,2,4,8,16,32,64,128,....
// 不是的話False ex. n % 2 餘數不是0,就失敗了
class Solution {
public:
    bool isPowerOfTwo(int n) {
        if(n<=0) return false;
        while(n>1){
            if(n%2 != 0) return false;
            n = n / 2;
        }
        return true;
    }
};
