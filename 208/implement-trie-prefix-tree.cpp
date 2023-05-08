class Trie {
public:
    Trie * next[26] = {};
    bool isWord = false;
    Trie() {
        
    }
    
    void insert(string word) {
//cout<<word<<endl;
        int i = word[0] - 'a';
//cout<<"i:"<<i<<endl;
        if(next[i]==nullptr) next[i] = new Trie();
        if(word.length()==1){
            next[i]->isWord = true;
        }else next[i]->insert(word.substr(1,word.length()-1));
    }
    
    bool search(string word) {
//cout<<"search:"<<word<<endl;
        if(word.length()==0) {return false;}
        int i = word[0] - 'a';
//cout<<"i:"<<i<<endl;
        if(next[i]==nullptr) {return false;}
        if(word.length()==1){
            if(next[i]->isWord) return true;
            else return false;
        }
        return next[i]->search(word.substr(1,word.length()-1));
    }
    
    bool startsWith(string prefix) {
        if(prefix.length()==0) return true;
        int i = prefix[0] - 'a';
        if(next[i]==nullptr) return false;
        return next[i]->startsWith(prefix.substr(1,prefix.length()-1));
    }
};
//case 12/16: ["Trie","insert","insert","insert","insert","insert","insert","search","search","search","search","search","search","search","search","search","startsWith","startsWith","startsWith","startsWith","startsWith","startsWith","startsWith","startsWith","startsWith"]
//[[],["app"],["apple"],["beer"],["add"],["jam"],["rental"],["apps"],["app"],["ad"],["applepie"],["rest"],["jan"],["rent"],["beer"],["jam"],["apps"],["app"],["ad"],["applepie"],["rest"],["jan"],["rent"],["beer"],["jam"]]
/**
 * Your Trie object will be instantiated and called as such:
 * Trie* obj = new Trie();
 * obj->insert(word);
 * bool param_2 = obj->search(word);
 * bool param_3 = obj->startsWith(prefix);
 */
