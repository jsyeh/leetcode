class Solution {
public:
    string tictactoe(vector<vector<int>>& moves) {
        int now = 1; //1:"A", 2:"B"
        int board[3][3] = {};
        string ans[3] = {"", "A", "B"};
        for(auto move : moves) {
            int i = move[0], j = move[1];
            board[i][j] = now;
            if(board[i][0]==board[i][1] && board[i][1]==board[i][2]) return ans[now];
            if(board[0][j]==board[1][j] && board[1][j]==board[2][j]) return ans[now];
            if(i==j && board[0][0]==board[1][1] && board[1][1]==board[2][2]) return ans[now];
            if(i+j==2 && board[2][0]==board[1][1] && board[1][1]==board[0][2]) return ans[now];

            now = 3 - now; //1=>2, 2=>1
        }
        if(moves.size()==9) return "Draw";
        return "Pending";
    }
};
