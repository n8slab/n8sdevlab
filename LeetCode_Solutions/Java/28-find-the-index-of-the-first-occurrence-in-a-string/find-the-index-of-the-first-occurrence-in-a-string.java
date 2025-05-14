class Solution {
    public int strStr(String haystack, String needle) {
        int x = haystack.length();
        int y = needle.length();

        for(int i=0; i<(x-y+1); i++){
            if(haystack.substring(i, i+y).equals(needle)){
                return i;
            }
        }

        return -1;
    }
}