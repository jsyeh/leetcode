// 總共只有 0, 10, 11 這3種解碼法, 像 Huffman Tree 的感覺
// 查查看 bits 能不能解碼，而且最後1個bit 0 一定只能是 0
// 就照著解碼即可
bool isOneBitCharacter(int* bits, int bitsSize) {
    int now = 1;  // 記錄剛剛解碼的，是 1 bit 或是 2 bits
    for(int i=0; i < bitsSize; i++) {
        if(bits[i]==0) {
            now = 1;  // 記得是位移1格
        } else {
            now = 2;  // 記得是位移2格
            i++;  // 要多移1格，才夠2格
        }
    }
    return now == 1;  // 是題目想要的「位移1格」嗎
}

