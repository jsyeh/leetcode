// 總共只有 0, 10, 11 這3種解碼法, 像 Huffman Tree 的感覺
// 查查看 bits 能不能解碼，而且最後1個bit 0 一定只能是 0
// 就照著解碼即可
class Solution {
public:
    bool isOneBitCharacter(vector<int>& bits) {
        for(int i=0; i<bits.size(); i++) {
            if(i==bits.size()-1) return true;  // 順利走到最後1位
            if(bits[i]==1) i++;  // 要多移1格，才夠2格
        }
        return false;  // 是走2格跳出的，false
    }
};

