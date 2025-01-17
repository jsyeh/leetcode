// LeetCode 2683. Neighboring Bitwise XOR
// derived[i] = original[i] XOR original[i+1]）
// 給你 derived 問「有沒有可能」有這樣的 original 陣列。
// 因XOR 做兩次=沒做，所以 derived 全部 XOR 起來 = original 全部 XOR 做兩次 = 0
bool doesValidArrayExist(int* derived, int derivedSize) {
    int total = 0; // 迴圈前面 total 是 0 
    for(int i=0; i<derivedSize; i++) {
        total ^= derived[i]; // 全部 XOR 起來，放入 total
    }
    return total==0; // 看最後 total 是不是 0     
}
