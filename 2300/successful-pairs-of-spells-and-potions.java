class Solution {
    public int[] successfulPairs(int[] spells, int[] potions, long success) {
        //1:23看懂題目，原來要把數字乘起來
        //直接乘 TLE
        //所以可以先把數字 potions sort
        //便可用binary search找到有幾組夠大
        int [] ans = new int[spells.length];
        Arrays.sort(potions);//我想知道比success少的有幾個，便能算反出合案
        for(int i=0; i<spells.length; i++){
            ans[i] = binarySearch(potions, 0, potions.length, success, spells[i]);
        }
        return ans;
    }
    int binarySearch(int[] potions, int i, int j, long success, long spell ){
        //右界j不包含，找出比val小的值，回傳比val小的值的數目
        if(i>=j) return (potions.length - i);//小心，剛好相等時怎麼辦
        int mid = (i+j)/2;
        if(success > potions[mid]*spell) return binarySearch(potions, mid+1, j, success, spell);
        else return binarySearch(potions, i, mid, success, spell);
    }
}
