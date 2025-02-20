class Solution {
    public int longestValidSubstring(String word, List<String> forbidden) {
       Set<String> invalid = new HashSet<>();

       for(String s : forbidden){
        invalid.add(s);
       }

       int n = word.length();
       int left = n-1;
       int right = left;
       int maxLength = 0;

       while(left> -1){
        for(int i=left; i<= Math.min(right, left + 9); i++){
            String substring = word.substring(left, i+1);

            if(invalid.contains(substring)){
                right = i-1;
                break;
            }
        }
        maxLength = Math.max(maxLength, right - left +1);
        left--;
       }

       return maxLength;


    }
}