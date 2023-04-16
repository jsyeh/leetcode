class Solution {
    public int search(int[] nums, int target) {
        //看完Editorial的講解後，試著做做看
        int index = myFindSmallest(nums, 0, nums.length-1);
System.out.println("index:"+index);
        int ans = -1;
        if(index==0) ans = Arrays.binarySearch(nums, target);
        else if(nums[0]<=target) ans = Arrays.binarySearch(nums, 0, index+1, target); //左半邊
        else ans = Arrays.binarySearch(nums, index, nums.length, target); //右半邊

        if(ans>=0) return ans;
        else return -1;
    }
    int myFindSmallest(int[] nums, int left, int right){
System.out.println("myfindSmallest:"+left+" "+right);
        if(nums[left]<nums[right]) return left;
        if(left==right) return left;

        int mid = (left+right)/2;
        //if(mid+1<right && nums[mid]>nums[mid+1]) {
        if(nums[mid]>nums[(mid+1)%nums.length]) {
            return (mid+1)%nums.length;
        }

        if(nums[left]<nums[mid]) { //normal 左邊很正常
            return myFindSmallest(nums, mid+1, right);
        } else { //左邊有奇怪的地方
            return myFindSmallest(nums, left, mid);
        }
    }
}//case 4: [1,3] 0
//case 5: [3,1] 0 我前一版在找 myfindSmallest()有寫錯
//case 6: [3,1] 3 
