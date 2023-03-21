class Solution {
    public void nextPermutation(int[] nums) {
        if(nums.length==1) return;
        int i = findChangingOne(nums);
        performNextOp(nums, i);
    }
    int findChangingOne(int [] nums) {
        int N = nums.length;
        for(int i=N-1-1; i>=0; i--) {
            if(nums[i]>=nums[i+1]){
                continue; //還不能拿來用
            }
            else{
                return i; //找到關鍵index了
            }
        }
        return -1;
    }
    void performNextOp(int [] nums, int k) {
        if(k==-1){//直接從小到大排好
            Arrays.sort(nums);
            return;
        }
        //find next bigger one num[k] < num[j]
        int one=k+1;
        for(int i=one+1; i<nums.length; i++){
            if(nums[k]<nums[i] && nums[i]<nums[one]) one = i;
        }
        int temp = nums[one];
        nums[one] = nums[k];
        nums[k] = temp;
        Arrays.sort(nums, k+1, nums.length);
/*        for(int i=k+1; i<nums.length; i++){
            for(int j=i+1; j<nums.length; j++){
                if(nums[i]>nums[j]){
                    int t2 = nums[i];
                    nums[i] = nums[j];
                    nums[j] = t2;
                }
            }
        }*/
    }
}//思考：[1,2], [2,1]
//思考：[1,2,3], [1,3,2], [2,1,3], [2,3,1], [3,1,2], [3,2,1], [1,2,3]...
//可能函式呼叫函式
//如果交換後沒比較大，那就要進位
// 3x2 = 6
// 4x3x2 = 24
// 100x...
//但偷看討論Discussion後， alexpoo 建議是，找到變小的數，把下一個數拿來用，之後再小到大排好
