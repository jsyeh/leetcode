class Solution {
    public int minSwaps(int[] data) {
        //因為Related Topics 寫 sliding window, 就將它設成1的個數
        int ones=0;
        for(int i=0; i<data.length; i++){
            if(data[i]==1) ones++; //一邊數1
            if(i>0) data[i] += data[i-1];//一邊做 prefix sum
        }
//System.out.println(ones);
        if(ones==0) return 0;//為了 [0,0,0] 全部都是0的狀況
        int ans = ones - data[ones-1];//如果ones是0的話，不能有這行
        for(int i=ones; i<data.length; i++){
            int temp = data[i]-data[i-ones];//目前範圍內1的數量
            if(ones-temp<ans) ans = ones-temp;
        }
        return ans;
    }//出錯的原因，可能是第0筆的資料沒算到, 所以修改第10行
}//case 35/36: [1,1,1,1,0,1,0,1,1,1,1,0,1,0,0,1,1,0,0,0,1,0,0,1,1,1,0,0,1,0,0,0,1,1,1,1,1,1,0,1,0,0,1,1,1,1,1,0,1,0,1,0,1,0,1,0,1,1,1,0,1,1,1,0,0,0,0,0,1,1,1,0,0,1,0,1,0,1,1,1,0,1,1,1,0,0,0,1,1,0,1,1,1,0,1,0,1,0,0,1,0,1,1,0,0,1,0,0,1,0,1,1,0,0,1,0,0,0,0,0,1,1,1,1,0,0,1,0,0,0,0,0,0,1,0,0,1,0,1,0,1,1,1,0,0,0,1,1,1,1,1,0,1,0,0,1,1,1,1,1,1,1,1,1,0,1,1,1,0,0,1,0,1,1,1,0,0,0,0,1,0,0,1,0,0,0,0,0,1,1,0,1,0,0,1,0,1,0,1,0]
