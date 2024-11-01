// LeetCode 3206. Alternating Groups I
// 環狀磚塊：0紅色 1藍色，任3個相鄰「色彩相間」很棒，有幾個？
int numberOfAlternatingGroups(int* colors, int colorsSize) {
    int ans = 0, N = colorsSize;
    for(int i=0; i<N; i++) {
        if(colors[i]!=colors[(i+1)%N] && colors[(i+1)%N]!=colors[(i+2)%N]) {
            ans++; // 相鄰3個不同色
        }
    }
    return ans;
}
