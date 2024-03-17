// 在 nums 裡，找「連續的subarray」裡面有一樣多的0和1
// 想像成「爬山」如果到達同一個高度，就代表「升1 降0」次數一樣
int findMaxLength(int* nums, int numsSize) {
    int H[200001]={}; // H[h] 第1次碰到高度h時的位置，0代表沒走過
    int now = 100000; //現在的高度，因「正負範圍」從100000開始跑
    int ans = 0;
    H[now] = 1; //最前面（出發時）的時間點
    for(int i=0; i<numsSize; i++){ //0-index
        if(nums[i]==1) now++; //往上昇
        else now--; //往下降
        //下面將 i(0-index) 改成 i+2(2-index)，因H[now]的初始值0對應「沒到訪過」
        if(H[now]==0) H[now] = i+2; //初次碰到，改成2-index
        else { // 要更新 ans 最大的距離
            if(i+2 - H[now] > ans) ans = i+2 -H[now];
        }
    }
    return ans;
}
