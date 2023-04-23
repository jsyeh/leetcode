class Solution {
    HashSet<List<Integer>> set = new HashSet<List<Integer>>();
    public List<List<Integer>> subsetsWithDup(int[] nums) {
        Arrays.sort(nums);
        return subset(nums, 0);
    }
    List<List<Integer>> subset(int[] nums, int start) {
        List<List<Integer>> ans = new ArrayList<List<Integer>>();
        if(start==nums.length){
            List<Integer> temp = new ArrayList<Integer>();
            ans.add(temp);
            return ans;
        }

        List<List<Integer>> lists = subset(nums, start+1);
        for(List<Integer> list : lists) {
            List<Integer> list1 = new ArrayList<Integer>();
            List<Integer> list2 = new ArrayList<Integer>();
            list1.addAll(list);
            list2.add(nums[start]);
            list2.addAll(list);
            print(list1);
            print(list2);
            //if(!set.contains(list1)) {
            //    System.out.println("contains list1");
            //    print(list1);
            //    set.add(list1);//如果這裡加入，則下一次就不會加入
                ans.add(list1);
            //}
            if(!set.contains(list2)) {
                System.out.println("contains list2");
                print(list2);
                set.add(list2);
                ans.add(list2);
            }
        }
        return ans;
    }
    void print(List<Integer> list){
        for(Integer i : list){
            System.out.print(i + " ");
        }
        System.out.println();
    }
}//case 15/20: [4,4,4,1,4]
