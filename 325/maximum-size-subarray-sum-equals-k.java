class Solution {
    public int maxSubArrayLen(int[] nums, int k) {
        int ans=0;;
        HashMap<Integer,Integer> map = new HashMap<>();
        map.put(0, -1);//全部都沒有的版本，index設-1
        for(int i=0; i<nums.length; i++) {
            if(i>0) nums[i] += nums[i-1]; //prefix sum
            
            if(map.containsKey(nums[i]-k)) {
                int index = map.get(nums[i]-k);
                if(i-index>ans) ans = i - index;
            }

            if(!map.containsKey(nums[i])) {
                map.put(nums[i], i);
            }//else不寫，因找最長，所以後面重覆的sum時，就不再存
        }
        return ans;
    }
}//case 33/36: [-1] -1
//case 35/36: [0,0] 0
