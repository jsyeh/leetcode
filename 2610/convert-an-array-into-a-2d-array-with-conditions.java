class Solution {
    public List<List<Integer>> findMatrix(int[] nums) {
        List<List<Integer>> ans2 = new ArrayList<List<Integer>>();
        Map<Integer,Integer> map = new HashMap<Integer,Integer>();//map.put(數字,次數);

        ArrayList<Integer> ans1 = new ArrayList<Integer>();
        //先數一下最多重覆的數字有幾次
        int maxRow=1;
        for(int i=0; i<nums.length; i++){
            if(!map.containsKey(nums[i])){
                map.put(nums[i], 1);
                ans1.add(nums[i]);
            }else{
                int repeat = map.get(nums[i])+1;
                map.put(nums[i], repeat);
                if(repeat>maxRow) maxRow=repeat;
            }
        }
        ans2.add(ans1);
        for(int i=1; i<maxRow; i++){
            ans2.add(new ArrayList<Integer>());
        }
        for(int i=0; i<ans1.size(); i++){
            int repeat = map.get(ans1.get(i));
            //System.out.println("repeat:"+repeat);
            for(int k=1; k<repeat; k++){
                ans2.get(k).add(ans1.get(i));
            }
        }

        
        return ans2;
    }
}
