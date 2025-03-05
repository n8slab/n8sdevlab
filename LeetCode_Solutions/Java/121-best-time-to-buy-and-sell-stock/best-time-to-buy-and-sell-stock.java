class Solution {
    public int maxProfit(int[] prices) {
        int buy = Integer.MIN_VALUE;
        int sold = 0;

        for(int price : prices){
            sold = Math.max(sold, buy + price);
            buy = Math.max(buy, -price);
        }

        return sold;
    }
}