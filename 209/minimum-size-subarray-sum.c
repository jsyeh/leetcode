//sliding window: 決定左界時，算出右界 O(n)
//binary search: 快速算出右界 O(log(n))
int minSubArrayLen(int target, int* nums, int numsSize){
    int N = numsSize;

    int sum[N+1]; //sum[i] 可了解 nums[0]...nums[i] 的加總值
    sum[0]=0;
    for(int i=1; i<=N; i++) sum[i] = sum[i-1] + nums[i-1];
    //nums[start]...nums[end] 加起來便是 sum[end+1] - nums[start];
    //可想像成 sum[end] - sum[start] 是右不包含、左包含
    //for(int i=0; i<=N; i++) printf("%d ", sum[i]);

    int ans = INT_MAX; //因為要找最小值，所以先設成最大值，以便替換
    int left = 0, right = N, mid = (right+left)/2;
    for(int start=0; start<N; start++){
        while(left<right){
            mid = (right+left)/2;
            int now = sum[mid] - sum[start];
            if(now==target){
                if(mid-start<ans) ans = mid-start;
                break; //離開while迴圈
            }else if(now>target){ //太大，往左走
                if(mid-start<ans) ans = mid-start;
                right = mid;
            }else left = mid + 1; //太小，往右走
        }
        if( sum[left]-sum[start] >= target && (left-start)<ans){
            ans = left-start;
        }
        right = N;
    }

    if(ans==INT_MAX) return 0;
    else return ans;
}
//原來題目是寫 greater than or equal to target 不是要相等
//case 7/20: 11
//[1,2,3,4,5]

