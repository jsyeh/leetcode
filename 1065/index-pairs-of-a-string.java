class Solution {
    public int[][] indexPairs(String text, String[] words) {

        Arrays.sort(words, (a,b)->(a.length()-b.length()));

        for(int i=0; i<words.length; i++) System.out.println(words[i]);

        ArrayList<ArrayList<Integer>> ans = new ArrayList<ArrayList<Integer>>();
        for(int i=0; i<text.length(); i++) {
            for(int k=0; k<words.length; k++) {
                if(words[k].length()>text.length()-i) continue;

                int bad=0;
                for(int j=0; j<words[k].length(); j++){
                    if(words[k].charAt(j)==text.charAt(i+j)){

                    } else {
                        bad=1;
                        break;
                    }
                }
                if(bad==0) {
                    ArrayList<Integer> temp = new ArrayList<Integer>();
                    temp.add(i);
                    temp.add(i+words[k].length()-1);
                    ans.add(temp);
                }
            }
        }

        int [][] ans2 = new int[ans.size()][2];
        for(int i=0; i<ans.size(); i++) {
            int [] temp = new int[2];
            temp[0] = ans.get(i).get(0);
            temp[1] = ans.get(i).get(1);
            ans2[i] = temp;
        }
        return ans2;
    }
}
