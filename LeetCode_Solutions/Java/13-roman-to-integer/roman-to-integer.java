class Solution {
    public int romanToInt(String s) {
        int result =0;
        int [] roman = new int[128];

        roman['I'] = 1;
        roman['V'] = 5;
        roman['X'] = 10;
        roman['L'] = 50;
        roman['C'] = 100;
        roman['D'] = 500;
        roman['M'] = 1000;

        for(int i=0; i<s.length()-1; i++){
            if(roman[s.charAt(i)] < roman[s.charAt(i+1)]){
                result -= roman[s.charAt(i)];
            }else{
                result += roman[s.charAt(i)];
            }
        }

        result += roman[s.charAt(s.length()-1)];

        return result;
    }
}