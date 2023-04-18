class Solution {
    public int subarraySum(int[] nums, int k) {
        int ans = 0;
        HashMap<Integer,Integer> map = new HashMap<Integer,Integer>();
        //把 nums[i] 的值, 變成 sum[i] 的意思

        map.put(0,1);
        //下面的迴圈,會少算一次(?), 所以要加上上面這筆,便能減最邊的邊界外
        for(int i=0; i<nums.length; i++){
            if(i>0) nums[i] += nums[i-1];

            if(map.containsKey(nums[i]-k)){
                ans += map.get(nums[i]-k);
            }
            //nums[i] - nums[old] == k, 
            // nums[old] = nums[i] - k;

            if(map.containsKey(nums[i])){
                map.put(nums[i], map.get(nums[i])+1);
            }else map.put(nums[i], 1);
        }
        return ans;
    }
}
// 1 1 1
// 1 2 3
//
