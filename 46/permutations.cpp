class Solution {
    public List<List<Integer>> permute(int[] nums) {
        //recursion
        ArrayList<Integer> array = new ArrayList<Integer>();
        for(int i=0; i<nums.length; i++){
            array.add(nums[i]);
        }
        return permute(array);
    }
    List<List<Integer>> permute(ArrayList<Integer> array) {
        List<List<Integer>> ans = new ArrayList<List<Integer>>();
        //if(array.size()==0) return;
        for(int i=0; i<array.size(); i++){
            ArrayList<Integer> subArray = new ArrayList<Integer>();
            if(array.size()==1){
                ans.add(array);
                return ans;
            }
            for(int k=0; k<array.size(); k++){
                if(k!=i) subArray.add(array.get(k));
            }
            List<List<Integer>> allList = permute(subArray);
            for(List<Integer> list : allList) {
                list.add(0, array.get(i));
                ans.add(list);
            }
        }
        return ans;
    }
}
