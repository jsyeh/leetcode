class Solution {
    public int longestArithSeqLength(int[] nums) {
        //意思是：等差數列， a[i] - a[i-1] 都是定值
        int n = nums.length;
        HashMap<Integer,Integer>[] table = new HashMap[n];
        //可以將 diff 對應到 次數

        int ans = 0;
        for(int right=0; right<n; right++){
            table[right] = new HashMap<>(); //table[i] 裡有 diff 及 次數
            int temp = 1; //如果考慮 right 為最後一個數，最佳的長度是 temp
            for(int left=0; left<right; left++){
                int diff = nums[right]-nums[left];
                if(table[left].containsKey(diff)){ //若幸運已有相同的diff值
                    int times = table[left].get(diff);
                    table[right].put(diff, times+1); //恭喜，+1
                    if(times+1>temp) temp = times+1;
                }else table[right].put(diff, 2);//最少也有2個
                if(2>temp) temp = 2;
            }
            if(temp>ans) ans = temp;
        }
        return ans;
    }
}
