class Solution {
    public boolean isSubsequence(String s, String t) {
        if(s.isEmpty()){
            return true;
        }

        int x =0;
        for(char c : t.toCharArray()){
            if(s.charAt(x) == c && ++x == s.length()){
                return true;
            }
        }

        return false;
    }
}