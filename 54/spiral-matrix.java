class Solution {
    public List<Integer> spiralOrder(int[][] matrix) {
        List<Integer> ans = new ArrayList<Integer>();
        int M = matrix.length, N = matrix[0].length;
        int left=0, right=N-1, up=0, down=M-1;
        int []dJ={1,0,-1,0};
        int []dI={0,1,0,-1};
        int dir=0, I=0, J=0;
        while(ans.size()<M*N){
//System.out.println("left:"+left+" right:"+right+" up:"+up+" down:"+down);
//System.out.println("I:"+I+" J:"+J+" Matrix[I][J]:"+matrix[I][J]);
            ans.add(matrix[I][J]);
            if(dir==0 && J==right){
                up++;
                dir = (dir+1)%4;
            }else if(dir==1 && I==down){
                right--;
                dir = (dir+1)%4;
            }else if(dir==2 && J==left){
                down--;
                dir = (dir+1)%4;
            }else if(dir==3 && I==up){
                left++;
                dir = (dir+1)%4;
            }
            I += dI[dir];
            J += dJ[dir];
        }
        return ans;
    }
}//case 4/23: [[3],[2]]
