long long maximumValueSum(int* nums, int numsSize, int k, int** edges, int edgesSize, int* edgesColSize) {
    long long min_diff = INT_MAX, move = 0, ans = 0;
    for(int i=0; i<numsSize; i++){
        int a = nums[i], b = nums[i] ^ k, diff = abs(a-b);
        if(diff<min_diff) min_diff = diff;
        if(b>a){
            move++;
            ans += b;
        }else ans += a;
    }
    if(move%2==1) ans -= min_diff;
    return ans;
}
