bool checkStraightLine(int** coordinates, int coordinatesSize, int* coordinatesColSize){
    if(coordinatesSize==2) return true;

    int x0 = coordinates[0][0], y0 = coordinates[0][1];
    int dx = coordinates[1][0]-x0, dy = coordinates[1][1]-y0;
    for(int i=1; i<coordinatesSize; i++){
        int x = coordinates[i][0], y = coordinates[i][1];
        if( (x-x0)*dy != (y-y0)*dx ) return false;
    }
    return true;
}
