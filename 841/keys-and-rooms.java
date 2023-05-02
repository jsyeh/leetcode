class Solution {
    public boolean canVisitAllRooms(List<List<Integer>> rooms) {
        int N = rooms.size();
        boolean [] visited = new boolean[N];

        visit(rooms, 0, visited);

        int visitedN=0;
        for(int i=0; i<N; i++){
            if(visited[i]) visitedN++;
        }
        if(visitedN == N) return true;
        else return false;
    }

    void visit(List<List<Integer>> rooms, int i, boolean [] visited) {
        if(visited[i]) return;
        visited[i] = true;
        List<Integer> keys = rooms.get(i);
        for(Integer next : keys){
            visit(rooms, next, visited);
        }
    }
}
