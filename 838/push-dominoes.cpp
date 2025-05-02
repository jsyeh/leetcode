// LeetCode 838. Push Dominoes
// 推「骨牌」：有 n 個骨牌排成一線, 每個骨牌可「往右推 or 往左推」
// 每隔一秒, 鄰近的1個骨牌會受影響而倒下。若剛好「左右鄰居都向你倒」就會保持中立/站立。
class Solution {
public:
    string pushDominoes(string dominoes) {
        int N = dominoes.length(); // 總共有 N 個骨牌
        int force[N]; // 用力量,來思考 往右倒的力,會是正的 (往左倒的力,是負的)
        int energy = 0;
        for(int i=0; i<N; i++){ // 往右的力
            if(dominoes[i]=='R') energy = N; // 同向, 充飽能量
            else if(dominoes[i]=='L') energy = 0; // 逆向, 能量沒了
            else if(energy>0) energy--; // 能量慢慢變小
            force[i] = energy;
        }
        energy = 0;
        for(int i=N-1; i>=0; i--){ // 往左的力
            if(dominoes[i]=='L') energy = N; // 充飽
            else if(dominoes[i]=='R') energy = 0; // 逆向, 能量沒了
            else if(energy>0) energy--;
            force[i] -= energy;

            if(force[i]==0) dominoes[i]='.'; // 再看最後的力,是中立、往右、往左
            else if(force[i]>0) dominoes[i] = 'R';
            else dominoes[i] = 'L';
        }
        return dominoes;
    }
};
