class Solution {
    public List<List<Integer>> threeSum(int[] nums) {
        List<List<Integer>> ans = new ArrayList<List<Integer>>();
        Arrays.sort(nums);
        for(int i=0; i<nums.length; ){
            twoSum(ans, nums, i, i+1, nums.length-1);
            int old = nums[i];
            while(i<nums.length && old==nums[i]){
                //System.out.print("."+nums[i]);
                i++;
            }
            //System.out.println();
        }
        return ans;
    }
    void twoSum(List<List<Integer>> ans, int[] nums, int target, int left, int right) {
        while(left<right){
            //System.out.print("=="+nums[target]+" "+nums[left]+" "+nums[right]);
            if(nums[left]+nums[right]+nums[target]==0){
                List<Integer> temp = new ArrayList<Integer>();
                temp.add(nums[target]);
                temp.add(nums[left]);
                temp.add(nums[right]);
                ans.add(temp);
                while(left<nums.length && temp.get(1)==nums[left]) left++;
                while(right>target && temp.get(2)==nums[right]) right--;
            }else if(nums[left]+nums[right]+nums[target]<0){
                left++;
            }else right--;
        }
    }
}//case 43/312: [0,0,0,0]
//case 42/312: [1,-1,-1,0]
//case 308/312: 3000個數字
