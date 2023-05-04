class Solution {

    int[] backup;
    int N;
    Random random = new Random();
    public Solution(int[] nums) {
        N = nums.length;
        backup = new int[N];
        for(int i=0; i<N; i++){
            backup[i] = nums[i];
        }
    }
    
    public int[] reset() {
        return backup;
    }
    
    public int[] shuffle() {
        //return backup; //在簡單測試資料裡, 直接 return backup 好像也可以通過
        //但是在 case 5/8: 5000個reset, 5000個shuffle, input 只有 [[-6, 10, 184]]

        //所以下面的方法有參考 Editorial
        List<Integer> waiting = new ArrayList<Integer>();
        for(int i=0; i<N; i++){
            waiting.add(backup[i]);
        }

        int[] ans = new int[N];
        for(int i=0; i<N; i++){
            int index = random.nextInt(N-i);
            ans[i] = waiting.get(index);
            waiting.remove(index);
            
        }
        return ans;
    }
}

/**
 * Your Solution object will be instantiated and called as such:
 * Solution obj = new Solution(nums);
 * int[] param_1 = obj.reset();
 * int[] param_2 = obj.shuffle();
 */
