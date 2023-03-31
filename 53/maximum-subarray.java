class Solution {
    //Kadane算法：在每一個掃描點計算以該點數值為結束點的子數列的最大和（正數和）
    //如果數列中含有負數元素，允許返回長度為零的子數列
    public int maxSubArray(int[] nums) {
        //因 subarray 定義成至少有1個，所以不能是0。nums.length>=1可用nums[0]
        //int max_sofar = 0, max_end_here = 0;
        int max_sofar = nums[0], max_end_here = nums[0];
        for(int i=1; i<nums.length; i++){
            max_end_here = max(nums[i], max_end_here + nums[i]);
                        //這裡從0改成nums[i] 表示斷開、新的開始
            max_sofar = max(max_sofar, max_end_here);
        }
        return max_sofar;
    }
    int max(int a, int b) {
        if(a>b) return a;
        else return b;
    }
}//case4: [-10]
//case5: [-2,1]
/*
    public int maxSubArray(int[] nums) {
        int [][] table = new int[nums.length+1][nums.length];
        //table[len][i] 長度len以內，連續 subarray，到i的最大sum
        for(int i=0; i<nums.length; i++){
            table[1][i] = nums[i]; //基礎表格，只用1個數
        }
        for(int len=2; len<=nums.length; len++){
            table[len][0] = table[len-1][0];
            for(int i=1; i<nums.length; i++){
                //方法不對，因為要加就要連續加，不能挑食
                int a = table[len-1][i];
                int b = table[len-1][i-1] + nums[i];
                int c = table[len][i-1];
                table[len][i] = max(a,b,c);
            }
        }
        return table[nums.length][nums.length-1];
    }
    int max(int a, int b, int c) {
        if(a>=b && a>=c) return a;
        if(b>=a && b>=c) return b;
        if(c>=a && c>=b) return c;
        return c;
    }*/
