class Solution {
    public boolean searchMatrix(int[][] matrix, int target) {
        int I=matrix.length, J=matrix[0].length;
        int [] array = new int[I*J];
        for(int i=0; i<I; i++){
            for(int j=0; j<J; j++){
                array[i*J+j] = matrix[i][j];
            }
        }
        int ans = Arrays.binarySearch(array, target);
        if(ans<0) return false;
        else return true;
    }
}
