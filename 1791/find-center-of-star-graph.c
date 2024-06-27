int findCenter(int** edges, int edgesSize, int* edgesColSize) {
    int a = edges[0][0], b = edges[0][1];
    if(a==edges[1][0] || a==edges[1][1]) return a;
    else return b;
}
