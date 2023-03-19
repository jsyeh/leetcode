class WordDictionary {
    //need tree data structure (tries)
    class TrieNode {
        TrieNode [] next = new TrieNode[26];
        boolean isWord;
        char c;
        TrieNode(char _c) {
            c = _c;
        }
        TrieNode() {
        }
    }

    TrieNode root;
    public WordDictionary() {
        root = new TrieNode();
    }
    
    public void addWord(String word) {
        int N = word.length();
        TrieNode now = root;
        for(int i=0; i<N; i++){
            char c = word.charAt(i);
            if(now.next[c-'a']==null){
                now.next[c-'a'] = new TrieNode(c);
            }
            now = now.next[c-'a'];
        }
        now.isWord = true;
    }

    public boolean search(String word) {
        return search(word, 0, root);
    }

    public boolean search(String word, int i2, TrieNode now) {
        int N = word.length();
        if(i2==N){
            return now.isWord;
        }
        char c = word.charAt(i2);
        if(c=='.'){
            for(int a=0; a<26; a++){
                if(now.next[a]!=null){
                    boolean found = search(word, i2+1, now.next[a]);
                    if(found) return true;
                }
            }
            return false;
        } else if(now.next[c-'a']==null) {
            return false;
        } else {
            return search(word, i2+1, now.next[c-'a']);
        }
    }

    public boolean search2(String word) {
        int N = word.length();
        TrieNode now = root;
        for(int i=0; i<N; i++){
            char c = word.charAt(i);
            if(c=='.'){
                for(int a=0; a<26; a++){
                    if(now.next[a]!=null){//任一個都行
                        //是否要改用函式呼叫函的寫法?
                    }
                }
            } else if(now.next[c-'a']==null){
                return false;
            } else {
                now = now.next[c-'a'];
            }
        }
        if(now.isWord) return true;
        return false;
    }
}

/**
 * Your WordDictionary object will be instantiated and called as such:
 * WordDictionary obj = new WordDictionary();
 * obj.addWord(word);
 * boolean param_2 = obj.search(word);
 */
