class Solution {
    public int distMoney(int money, int children) {
        int c = children;
        //先把money減掉children
        //剩下的，希望都是7,但不能是3，看能怎麼分
        //20: 8,9,3
        //16: 8,8
        if(money/children==8 && money%children==0) return children;
        //剛好平分8元
        
        if(money/children>=8) return children-1;
        //有1人超過8元，其它都是8元
        
        //以下，則是不夠分，所以看有幾個人夠8
        //先每人分1元, 接下來再看夠幾個 
        int remain = money-children;
        //money -= children;
        if(remain<0) return -1;//不夠分，悲
        if(money==4 && c==1) return -1; //不能1人4元
        
        int ans = remain/7;//剩3種可能
        if(remain%7!=3) return ans;
//        if(remain%7==3){
//            if(ans>0)
//        }
        
        if(remain%7==3 && ans>0 && children-ans==1) ans--;
        if(remain%7!=0 && ans>0 && ans==children) ans--;
        return ans;
    }
}
//5
//2 => 0
//13
//3 => 1 10%7=1
//17 : 8,9
//2 => 1 15%7=2...1. 
//23
//2 => 1 
//71
//8 => 7
