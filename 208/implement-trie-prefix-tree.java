class Node {
    Node [] table= new Node[26];
    boolean end;
    Node() {
        for(int i=0; i<26; i++){
            table[i]=null;
        }
        end = false;
    }
}
class Trie {
    Node root;
    public Trie() {
        root = new Node();
    }
    
    public void insert(String word) {
        Node now = root;
        for(int i=0; i<word.length(); i++){
            char c = word.charAt(i);
            if(now.table[c-'a']==null){
                now.table[c-'a']=new Node();
            }
            now = now.table[c-'a'];
        }
        now.end = true;
    }
    
    public boolean search(String word) {
        Node now = root;
        for(int i=0; i<word.length(); i++){
            char c = word.charAt(i);
            if(now.table[c-'a']==null) return false;
            now = now.table[c-'a'];
        }
        if(now.end) return true;
        else return false;
    }
    
    public boolean startsWith(String prefix) {
        Node now = root;
        for(int i=0; i<prefix.length(); i++){
            char c = prefix.charAt(i);
            if(now.table[c-'a']==null) return false;
            now = now.table[c-'a'];
        }
        return true;
    }
}

/**
 * Your Trie object will be instantiated and called as such:
 * Trie obj = new Trie();
 * obj.insert(word);
 * boolean param_2 = obj.search(word);
 * boolean param_3 = obj.startsWith(prefix);
 */
