int min(int a, int b){
    if(a>b) return b;
    else return a;
}
long long countSubarrays(int* nums, int numsSize, int minK, int maxK){
    //下面的程式, 是參考 https://leetcode.com/problems/count-subarrays-with-fixed-bounds/solutions/2707995/simple-o-n-c-solution/ 的解題概念
    long long ans = 0;
    bool minFound = false, maxFound = false;
    int start = 0, minStart = 0, maxStart = 0;
    for(int i=0; i<numsSize; i++){
        int now = nums[i];
        if(now < minK || now > maxK){ //超過範圍, 糟! 重來!
            minFound = false;
            maxFound = false;
            start = i+1; //要有新的 start index 值, 不能對應到範圍外的數
        }
        //下面不能用else if 因會導致 minK == maxK 時, 會有一個沒更新到
        if(now == minK){
            minFound = true;
            minStart = i; //對應到 min 的index值
        }
        if(now == maxK){
            maxFound = true;
            maxStart = i;
        }

        if(minFound && maxFound){//恭喜,兩個都成立,表示現在的這段Subarray是合乎規定的
            //如果Subarray 結束在 i 這裡, 那開始是在哪裡呢? 可以是 start 到 {minStart,maxStart} 間的任一處開始
            int start2 = min(minStart, maxStart);
            ans += start2 - start + 1; //種樹問題, 開頭到底有幾種可能的位置, 就 樹的間隔+1
        }
    }
    return ans;
}
