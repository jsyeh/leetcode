class Solution {
public:
    int table[3][3] = {};
    bool testWin() {
        for(int i=0; i<3; i++){
            int A = 0, B = 0;
            for(int j=0; j<3; j++){
                if(table[i][j]==-1) A++;
                if(table[i][j]==+1) B++;
            }
            if(A==3 || B==3) return true;
        }
        for(int j=0; j<3; j++){
            int A = 0, B = 0;
            for(int i=0; i<3; i++){
                if(table[i][j]==-1) A++;
                if(table[i][j]==+1) B++;
            }
            if(A==3 || B==3) return true;
        }
        int A = 0, B = 0, A2 = 0, B2 = 0;
        for(int i=0; i<3; i++){
            if(table[i][i]==-1) A++;
            if(table[i][i]==+1) B++;
            if(table[i][2-i]==-1) A2++;
            if(table[i][2-i]==+1) B2++;
        }
        if(A==3 || B==3 || A2==3 || B2==3) return true;
        return false;
    }
    string tictactoe(vector<vector<int>>& moves) {
        int d[] = {-1, +1};
        for(int i=0; i<moves.size(); i++){
            int ii = moves[i][0], jj = moves[i][1];
            table[ii][jj] = d[i%2];
            if(testWin()){
                if(i%2==0) return "A";
                else return "B";
            }
        }
        if(moves.size()==9) return "Draw";
        else return "Pending";
    }
};
