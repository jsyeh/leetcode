class Solution {
    ArrayList<String> pathParts = new ArrayList<String>();
    int dot = 0;
    String name = "";
    public String simplifyPath(String path) {
        for(int i=0; i<path.length(); i++) {
            char c = path.charAt(i);
            if(c=='.' && name.equals("")) dot++;
            else if(c=='/'){
                process();
            } else{
                for(int k=0; k<dot; k++) name += ".";
                name += c;
                dot=0;
            }
        }
        process();

        if(pathParts.size()==0) return "/";
        String ans="";
        for(int i=0; i<pathParts.size(); i++){
            ans += "/" + pathParts.get(i);
        }
        return ans;
    }
    void process(){
System.out.println("name:"+name+" dot:"+dot);
        if(dot==2){
            if(pathParts.size()>0) pathParts.remove(pathParts.size()-1);
        } else if(dot==1) {}
        else if(name.equals("") && dot==0) {}
        else {
            for(int k=0; k<dot; k++) name += ".";
            dot=0;
            pathParts.add(name);
        }
        name="";
        dot=0;
    }
}
/*class Solution {
    public String simplifyPath(String path) {
        //ArrayList<Character> ans = new ArrayList<Character>();
        ArrayList<String> pathParts = new ArrayList<String>();

        char c=' ', prev=' ', prevprev=' ';
        int dot=0;
        String name="";
        for(int i=0; i<path.length(); i++) {
            prevprev = prev;
            prev = c; 
            c = path.charAt(i);
            boolean valid=(c!='.' && c!='/');

            if(c=='.') dot++;

for(int k=0; k<pathParts.size(); k++){
    System.out.print("/"+pathParts.get(k));
}
System.out.println();
System.out.println(" dot:"+dot+" name:"+name+" c:"+c);

            if(valid){
                for(int k=0; k<dot; k++){
                    name += ".";
                }
                dot=0;
                name += c;
            }else if(c=='/' &&  prev=='/'){
                //不做事，因為一個斜線就可以了
            }else if(c=='/'){
                if(dot==2 && name.equals("")){ // .. 表示要到前一個目錄
                    if(pathParts.size()==1){ }//已是 root 就不再刪
                    else pathParts.remove(pathParts.size()-1);//刪除最後1個
                    dot=0;
                }else if(dot==1 && name.equals("")){
                    // . 表示這個目錄，沒事，不管它
                    dot=0;
                }else {
                    for(int k=0; k<dot; k++){
                        name += ".";
                    }
                    dot=0;

                    pathParts.add(name);//Q:若加入後,再改變name,會影響ArrayList值嗎？
                    name = "";
                }
                name = "";//遇到第1個斜線，就可以把name加到ArrayList裡
            }//else if(c=='.' && prev=='.' && prevprev=='.'){
             //   if(dot==3) name += "...";//變成檔名 dot dot dot 一起上
             //   else name += ".";//4個以上，再逐個加dot
            //}

            if(c!='.') dot = 0;
        }

        if(dot==2 && !name.equals("") && pathParts.size()!=1) pathParts.remove(pathParts.size()-1);//最後的 .. 也要退一步
        //else if(dot>2) pathParts.add(name);//最後是 ...則是要加到名字中
        else if(c!='/'){//}if(name.length()>1){
            if(dot>2){
                for(int k=0; k<dot; k++){
                    name += ".";
                }
                dot=0;
            }
            pathParts.add(name);
        }
        if(pathParts.size()==1) return "/";

        String ans="";
        for(int i=1; i<pathParts.size(); i++){
            if(pathParts.get(i).equals("") && i!=1) continue;
            ans += "/" + pathParts.get(i);
        }
        return ans;

    }
}
*/
//case4: "/a/./b/../../c/"
//case5: "/a//b////c/d//././/.."
//也就是最後結尾時的 .. 也要做動作
//case6: "/.."
//case7: "/..."
//case8: "/..hidden"
//case9: "/.....hidden"
//case10: "/home/of/foo/../../bar/../../is/./here/."
//case11: "/a//b.."

/*
"/..//"
"/a/./b/../../c/"
"/a//b////c/d//././/.."
"/.."
"/..."
"/..hidden"
"/.....hidden"
"/home/of/foo/../../bar/../../is/./here/."
*/
