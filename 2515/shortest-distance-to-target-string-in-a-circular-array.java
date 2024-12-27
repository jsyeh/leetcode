// LeetCode 2515. Shortest Distance to Target String in a Circular Array
// 有100個字串，你從 startIndex 出發，可往右、往左，最快多久可遇到 target 字串
class Solution {
    public int closetTarget(String[] words, String target, int startIndex) {
        int N = words.length;
        for(int i=0; i<N; i++) {
            int i1 = (startIndex+i) % N; // 往右的 index 
            int i2 = (startIndex+N-i) %N; // 往左的 index
            if(words[i1].equals(target)) return i; // 往右有找到
            if(words[i2].equals(target)) return i; // 往左有找到
        }
        return -1; // 找不到
    }
}
