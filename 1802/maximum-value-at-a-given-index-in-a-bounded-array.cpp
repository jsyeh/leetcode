class Solution {
public:
    int maxValue(int n, int index, int maxSum) {
        //int nums[n];
        //因為n可能超級大，所以無法開陣列
        //想像 num[index]被拉到最大，同時面積<maxSum
        //就像蚊帳有一個點被拉得很高，面積不能超過maxSum
        //所以左邊都比它小，右邊也都比它小
        //或許可以用 binary search 的技巧，來找到 num[index]的值
        //需要 area(n, index, height)<=maxSum
        //同時沒有拉起來的值都還有1
        int left=1, right=maxSum+1; //本來我寫 right=INX_SUM 但看 lee215 解法，可不用太大
        //不過在 case 44/370: 1 0 24 等於有個 101大樓，
        //如果right=maxSum時，就會錯過 maxSum的答案。所以right=maxSum+1
        while(left+1<right){
            int mid = (left+right)/2;
            unsigned long long int a = area(n, index, mid);
printf("left:%d mid:%d a:%d right:%d\n", left, mid, a, right);
            if(a==maxSum) return mid;
            if(a>maxSum) right = mid;
            else left = mid;
        }
printf("left:%d right:%d\n", left, right);
        return left;
    }

    unsigned long long int area(int n, int index, int height) {
        // 1, 1+2, 1+2+3, ... 所以三角形/梯形的面積，是 (h+1)*h/2 含本身
        // 或是 (h+h-index)*(index+1)/2
        //另一個方向 (h+1)*h/2 或是 (h+h-index)*(index+1)/2 其中 index換成 n-1-index
        unsigned long long h = height-1; //case 52/370 因 height: 90924720 乘出來會太大，改成long
        unsigned long long left = (h+1)*h/2, right = (h+1)*h/2; //簡單的 3,2,1 有走完
        if(index<h) left = (h+h-index)*(index+1)/2;
        if(n-1-index<h) right = (h+h-(n-1-index))*(n-1-index+1)/2;
        return n+left+right-h;
  }
};
//case 44/370: 1 0 24
//case 52/370: 9 0 90924720 要改用 long long 
//case 106/370: 6 2 931384943 要把 area 相關都改成 unsigned long long
