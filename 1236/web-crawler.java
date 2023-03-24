/**
 * // This is the HtmlParser's API interface.
 * // You should not implement it, or speculate about its implementation
 * interface HtmlParser {
 *     public List<String> getUrls(String url) {}
 * }
 */

class Solution {
    Set<String> set;
    List<String> ans;
    String hostname;
    public List<String> crawl(String startUrl, HtmlParser htmlParser) {
        set = new HashSet<String>();
        ans = new ArrayList<String>();
        int end = startUrl.indexOf('/', 7);
        if(end==-1) hostname = startUrl;
        else hostname = startUrl.substring(0, end);
        set.add(startUrl);
        ans.add(startUrl);
        myCrawl(startUrl, htmlParser);
        return ans;
    }
    void myCrawl(String startUrl, HtmlParser htmlParser) {
        List<String> list = htmlParser.getUrls(startUrl);
        for(String now : list) {
            if(!set.contains(now) && now.indexOf(hostname)!=-1) {
                set.add(now);
                ans.add(now);
                myCrawl(now, htmlParser);
            }
        }
    }
}
