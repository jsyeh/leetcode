class Solution {
    public int[] twoSum(int[] nums, int target) {
        Map<Integer,Integer> map = new HashMap<Integer,Integer>();
        for(int i=0; i<nums.length; i++){
            int another = target - nums[i];
            if(map.containsKey(another)) {
                int [] ans = new int[2];
                ans[0] = map.get(another);
                ans[1] = i;
                return ans;
            }
            map.put(nums[i], i);
        }
        return null;
    }
}
