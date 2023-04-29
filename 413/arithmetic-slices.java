class Solution {
    public int numberOfArithmeticSlices(int[] nums) {
        int N = nums.length;
        for(int i=0; i<N-1; i++) {
            nums[i] = nums[i+1] - nums[i];
        }

        int combo=0, ans=0;
        for(int i=0; i<N-1-1; i++){
            if(nums[i]==nums[i+1]) { //2個差別相同，表示連續3個數合格
                combo++;
            }else{
                ans += combine(combo);
                combo = 0;
            }
        }
        ans += combine(combo);
        return ans;
    }
    int combine(int combo){
        //combo 1: 1
        //combo 2: 1 + 2
        //combo 3: 1 + 2 + 3
        return (1+combo)*combo/2;
    }
}
