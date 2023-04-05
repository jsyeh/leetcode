class Solution {
    public int minimizeArrayValue(int[] nums) {
        //02:01看懂，可能用
        long runningSum=nums[0];
        long ans = runningSum;
        int N = nums.length;
        for(int i=1; i<N; i++){
            runningSum += nums[i];
            if(runningSum/(i+1.0)>ans){
                ans = runningSum/ (i+1);
                if(runningSum%(i+1)>0) ans++;
            }
/*            if(nums[i-1]>=nums[i]){
                //沒辦法移，就記下此時的最大值
                if(num[i-1]>ans) ans = num[i-1];
            }else{
                //4:25再度卡住，好像不能暴力法 07:15放棄
            }*/
        }
        return (int)ans;
    }//Idea: Run-length, 邊讀邊平均它的值，restart
}//case 3: 大量數字，可能加出來的結果大於32bit
