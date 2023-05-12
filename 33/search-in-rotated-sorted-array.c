//還沒寫完，有留遺憾
int myFindSmallest(int* nums, int N, int left, int right){
printf("myfindSmallest: %d %d\n", left, right);
    if(nums[left]<nums[right]) return left;
    if(left==right) return left;

    int mid = (left+right)/2;
    //if(mid+1<right && nums[mid]>nums[mid+1]) {
    if(nums[mid]>nums[(mid+1)%N]) {
        return (mid+1)%N;
    }

    if(nums[left]<nums[mid]) { //normal 左邊很正常
        return myFindSmallest(nums, N, mid+1, right);
    } else { //左邊有奇怪的地方
        return myFindSmallest(nums, N, left, mid);
    }
}
int binarySearch(int * nums, int target, int left, int right){
    while(left<right){
        int mid = (left+right)/2;
        if(nums[mid]==target) return mid;
        if(nums[mid]<target){
            left = mid + 1;
        }else right = mid;
    }
    return left;
//    if(nums[left]==target) return left;
//    else return -1;
}
int search(int* nums, int numsSize, int target){
    //之前看完Editorial的講解後，有用 Java 做出來。現在翻譯成 C 看看
    int index = myFindSmallest(nums, numsSize, 0, numsSize-1);
printf("index:%d\n", index);
    int ans = -1;
    if(index==0) ans = binarySearch(nums, target, 0, numsSize);
    else if(nums[0]==target) ans = 0;
    else if(nums[0]<=target) ans = binarySearch(nums, target, 0, index); //左半邊
    else ans = binarySearch(nums, target, index, numsSize); //右半邊
printf("ans:%d\n", ans);
    if(ans>=0 && ans<numsSize && nums[ans]==target) return ans;
    else return -1;
}//case 4: [1,3] 0
//case 5: [3,1] 0 我前一版在找 myfindSmallest()有寫錯
//case 6: [3,1] 3 
//case 189/195: [4,5,6,7,0,1,2] 7
