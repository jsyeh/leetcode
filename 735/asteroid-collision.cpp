class Solution {
public:
    vector<int> asteroidCollision(vector<int>& stones) {
        stack<int> ans;
        for(int i=0; i<stones.size(); i++){
            int now = stones[i];
            if(now<0){ //往左的行星
                //看看看左邊有沒有人往右移，有的話就碰撞
                while(ans.size()>0 && ans.top()>0){ //左邊的會過來相撞
                    int left = ans.top();
                    ans.pop();
                    if(left+stones[i]>0){
                        ans.push(left);
                        now=0;
                        break; //左邊大，原本左邊的石頭留著
                    }else if(left+stones[i]==0){
                        now=0;
                        break; //兩顆石頭一起消失
                    }else{
                        //右邊大，繼續往左邊撞
                    }
                }
                if(now!=0) ans.push(now);
            }else ans.push(now); //往右的行星，
        }

        vector<int> ans2(ans.size());
        for(int i=ans.size()-1; i>=0; i--){
            ans2[i] = ans.top();
            ans.pop();
        }
        return ans2;
    }
};
