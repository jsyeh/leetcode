class Solution {
    public int numSteps(String s) {
        int ans = 0;
        int len = s.length();
        int [] bit = new int[len];
        for(int i=0; i<len; i++){
            bit[i] = s.charAt(i)-'0';
        }
        int carry=0;
        //最高bit更前面的bit, 以避免 111111 + 1 之後爆炸的問題, 這時直接回答 ans += 1的數量+1即可
        while(len>1) {
            //print(bit);
            if(bit[len-1]==0){ //除以2
                len--;
            } 
            else {
                for(int i=len-1; i>=0; i--) { //加1
                    if(bit[i]==0){
                        bit[i] = 1;
                        for(int k = i+1; k<len; k++) bit[k] = 0;
                        break;
                    }else if(i==0){ ///一堆1 讓它爆炸, 這時候直接算出合案
                        ans += len+1;
                        return ans;
                    }
                }
            }
            ans++;
        }

        return ans;
    }
    void print(int [] bit) {
        for(int i=0; i<bit.length; i++){
            System.out.print(bit[i]);
        }
        System.out.println();
    }
}
