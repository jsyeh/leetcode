class Solution {
    public int[] arrayChange(int[] nums, int[][] operations) {
        Map<Integer, Integer> mapFrom = new HashMap<Integer, Integer>();
        Map<Integer, Integer> mapTo = new HashMap<Integer, Integer>();
        for(int i=0; i<nums.length; i++){
            mapFrom.put(nums[i], nums[i]);
            mapTo.put(nums[i], nums[i]);
        }
        for(int i=0; i<operations.length; i++){
            int from = operations[i][0];
            int to = operations[i][1];
            int realFrom = mapFrom.get(from);

            mapTo.put(realFrom,to);

            mapFrom.put(to,realFrom);
            //mapFrom.remove(to);
            //table[a] = b; //這個方法也不對，因為時間前後會有不同的影響
            //不過題目好像暗示 distinct 表示都不會重覆,因為目標一定不會重覆
        }
        for(int i=0; i<nums.length; i++){
            nums[i] = mapTo.get(nums[i]);
        }

        return nums;
        //nums vs. operations 也是不能暴力，因 10^10
        /*int [] table = new int[1000001];
        for(int i=0; i<table.length; i++){
            table[i] = i;
        }
        for(int i=0; i<operations.length; i++){
            int a = operations[i][0];
            int b = operations[i][1];
            table[a] = b; //這個方法也不對，因為時間前後會有不同的影響
            //不過題目好像暗示 distinct 表示都不會重覆,因為目標一定不會重覆
        }*/
    }
}
