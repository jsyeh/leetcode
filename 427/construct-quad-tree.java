/*
// Definition for a QuadTree node.
class Node {
    public boolean val;
    public boolean isLeaf;
    public Node topLeft;
    public Node topRight;
    public Node bottomLeft;
    public Node bottomRight;

    
    public Node() {
        this.val = false;
        this.isLeaf = false;
        this.topLeft = null;
        this.topRight = null;
        this.bottomLeft = null;
        this.bottomRight = null;
    }
    
    public Node(boolean val, boolean isLeaf) {
        this.val = val;
        this.isLeaf = isLeaf;
        this.topLeft = null;
        this.topRight = null;
        this.bottomLeft = null;
        this.bottomRight = null;
    }
    
    public Node(boolean val, boolean isLeaf, Node topLeft, Node topRight, Node bottomLeft, Node bottomRight) {
        this.val = val;
        this.isLeaf = isLeaf;
        this.topLeft = topLeft;
        this.topRight = topRight;
        this.bottomLeft = bottomLeft;
        this.bottomRight = bottomRight;
    }
};
*/

//如果subtree全部都一樣val，那可以簡化成 (1,val) 讓它變成 isLeaf=1
//這樣空間就會很省
class Solution {
    public Node construct(int[][] grid) {
        int N = grid.length; //最大是 2^6＝64
        return subTree(grid, 0, N, 0, N, N);
    }
    Node subTree(int[][] grid, int i0, int i1, int j0, int j1, int N) {
        //i0..i1(不包含), j0...j1(不包含)
        if(N==1) {//}(i0+1==i1 && j0+1==j1) { //最小單位
            return new Node(grid[i0][j0]==1, true); //isLeaf
            //題目 input 把 1 都當成是 true, 所以用 ==1 當成值
        }
        Node n1 = subTree(grid, i0, i0+N/2, j0, j0+N/2, N/2);
        Node n2 = subTree(grid, i0, i0+N/2, j0+N/2, j1, N/2);
        Node n3 = subTree(grid, i0+N/2, i1, j0, j0+N/2, N/2);
        Node n4 = subTree(grid, i0+N/2, i1, j0+N/2, j1, N/2);
        boolean allLeaf = n1.isLeaf && n2.isLeaf && n3.isLeaf && n4.isLeaf;
        if(allLeaf && n1.val==n2.val && n2.val==n3.val && n3.val==n4.val) {
            return new Node(n1.val, true); //isLeaf
        }
        return new Node(true, false, n1, n2, n3, n4);
    }
}

