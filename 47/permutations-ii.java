class Solution {
    public List<List<Integer>> permuteUnique(int[] nums) {
        List<List<Integer>> ans = new ArrayList<List<Integer>>();
        Arrays.sort(nums);
        boolean [] used = new boolean[nums.length];
        List<Integer> temp = new ArrayList<Integer>(nums.length);
        permute(nums, 0, ans, used, temp);
        return ans;
    }

    void permute(int[] nums, int start, List<List<Integer>> ans, boolean [] used, List<Integer> temp) {
        if(start==nums.length-1) { //位數到了，可以收成
            for(int i=0; i<nums.length; i++) {
                if(!used[i]) {
                    temp.add(nums[i]);
                    List<Integer> temp2 = new ArrayList<Integer>(temp);
                    ans.add(temp2);
                    temp.remove(temp.size()-1);
                    return;
                }
            }
        }
        int prev=Integer.MIN_VALUE;
        for(int i=0; i<nums.length; i++) {
            if(!used[i] && prev!=nums[i]){ //這個為首沒用過，太好了
                prev = nums[i];
                temp.add(nums[i]);
                used[i] = true;
                permute(nums, start+1, ans, used, temp );
                temp.remove(temp.size()-1);
                used[i] = false;
            }
        }
    }
}
