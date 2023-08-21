// 先找到 pivot位置, 再去找
class Solution {
    public boolean search(int[] nums, int target) {
        //find pivot, 但問題在,可能會相同, 所以不能直接 binary search
        int N = nums.length;
        if(N==1) return nums[0]==target;
        int left = 0, right = N;
        while(left<right){
            int mid = (left+right)/2;
            if(nums[mid]==target) return true;
            if(nums[mid]==nums[left]){ // 這裡要改，才滑得正確
                left++; // 如果找到相同,必須往右滑動
                continue; // 要再重覆測試以往右移
            }
            if(nums[0] < nums[mid]) left = mid+1; // 要與 nums[0] 比較
            else right = mid;
        } 
        //System.out.println(nums[left] + " left:" + left);
        int pivot = left;
System.out.println(pivot);

        left = 0;
        right = N;
        while(left<right){
            int mid = (left+right)/2, mid2 = (mid+pivot)%N;
System.out.println(left +" "+ right +" "+ mid);
            if(nums[mid2]==target) return true;
            if(nums[mid2]<target){
                left = mid+1;
            }else right = mid;
        }
        if(nums[(left+pivot)%N]==target) return true;
        else return false;
    }
}
//case 2/280: [1] 1
//case 3/280: [1,0,1,1,1] 0
//case 265/280: [1,1,1,1,1,1,1,1,1,1,1,1,1,2,1,1,1,1,1] 2
//case 268/280: [2,2,2,3,2,2,2] 3
//caes 276/280: [4,5,6,7,0,1,2] 0
