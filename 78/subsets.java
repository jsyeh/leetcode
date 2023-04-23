class Solution {
    public List<List<Integer>> subsets(int[] nums) {
        //List<List<Integer>> ans = new ArrayList<List<Integer>>();
        return subset(nums, 0);
        //return ans;
    }
    List<List<Integer>> subset(int[] nums, int start) {
        ArrayList<List<Integer>> ans = new ArrayList<List<Integer>>();
        if(start==nums.length){
            ans.add(new ArrayList<Integer>());
            return ans;
        }
        List<List<Integer>> sub = subset(nums, start+1);
        for(List<Integer> list : sub) {
            List<Integer> list1 = new ArrayList<Integer>();
            List<Integer> list2 = new ArrayList<Integer>();
            list1.addAll(list);
            list2.add(nums[start]);
            list2.addAll(list);
            ans.add(list1);
            ans.add(list2);
        }
        return ans;
    }
}
