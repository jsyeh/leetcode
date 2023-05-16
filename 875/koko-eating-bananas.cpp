class Solution {
public:
    bool canEatInTime(vector<int>& piles, int h, int speed){
        int t = 0;
        for(int bananas : piles) {
            if(bananas<=speed) t++;
            else{
                t += bananas/speed;
                if(bananas%speed>0) t++;
            }
        }
        if(t<=h) return true;
        else return false;
    }
    int minEatingSpeed(vector<int>& piles, int h) {
        sort(piles.begin(), piles.end());
        int left = 1, right = piles[piles.size()-1];
        while(left<right){
            int mid = (left+right)/2;
            if(canEatInTime(piles, h, mid)){
                right = mid;
            }else{
                left = mid + 1;
            }
        }
        return left;
    }
};
