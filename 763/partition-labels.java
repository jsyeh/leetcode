class Solution {
    public List<Integer> partitionLabels(String s) {
        //每個字母有開始、結束，所以就查26個字母的overlap interval
        int N = s.length();
        int [][] p = new int[26][2];
        for(int i=0; i<26; i++){
            p[i][0] = Integer.MAX_VALUE;
            p[i][1] = Integer.MIN_VALUE;
        }
        for(int i=0; i<N; i++) {
            int k = s.charAt(i)-'a';
            p[k][0] = Math.min(p[k][0], i);
            p[k][1] = Math.max(p[k][1], i);
        }

        Arrays.sort(p, (a,b)->a[0]-b[0]);
        int pN = 26;
        for(int i=0; i<26; i++){
            if(p[i][0]==Integer.MAX_VALUE) {pN = i; break;}
        }
        for(int i=0; i<pN; i++){
            System.out.println(p[i][0] + " " + p[i][1]);
        }

        List<Integer> ans = new ArrayList<Integer>();
        int left=p[0][0], right=p[0][1];
        for(int i=1; i<pN; i++){
            if(p[i][0]>right) {
                //output ne answer
                ans.add(right-left+1);
                left = p[i][0];
                right = p[i][1];
            }else if(p[i][1]>right){
                right = p[i][1];
            }
        }
        ans.add(right-left+1);
        return ans;
    }
}//case 43/118: "ntswuqqbidunnixxpoxxuuupotaatwdainsotwvpxpsdvdbwvbtdiptwtxnnbtqbdvnbowqitudutpsxsbbsvtipibqpvpnivottsxvoqqaqdxiviidivndvdtbvadnxboiqivpusuxaaqnqaobutdbpiosuitdnopoboivopaapadvqwwnnwvxndpxbapixaspwxxxvppoptqxitsvaaawxwaxtbxuixsoxoqdtopqqivaitnpvutzchkygjjgjkcfzjzrkmyerhgkglcyffezmehjcllmlrjghhfkfylkgyhyjfmljkzglkklykrjgrmzjyeyzrrkymccefggczrjflykclfhrjjckjlmglrmgfzlkkhffkjrkyfhegyykrzgjzcgjhkzzmzyejycfrkkekmhzjgggrmchkeclljlyhjkchmhjlehhejjyccyegzrcrerfzczfelzrlfylzleefgefgmzzlggmejjjygehmrczmkrc"
