class Solution {
    public int smallestRangeII(int[] nums, int k) {
        Arrays.sort(nums);
        int ans = nums[nums.length-1] - nums[0]; //如果全部都加k or 都減k,答案不變

        //想像,最左邊+k, 最右邊-k, 中間的+k,中間的-k 這幾個數,競爭max,min
        int left = nums[0] + k, right = nums[nums.length-1] - k;
        for(int i=0; i<nums.length-1; i++) {//這個 a[i] 是轉折點, 左邊+k, 右邊-k
            int min = left, max = right;
            if(nums[i]+k > right) max = nums[i] + k;
            if(nums[i+1]-k < left) min = nums[i+1] - k;
            if(max-min<ans) ans = max - min;
        }

        return ans;
    }
}
