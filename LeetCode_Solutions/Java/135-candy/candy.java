class Solution {
    public int candy(int[] ratings) {
        int n = ratings.length;
        int startRate = 1;
        int candyCount = 0;

        //Using greedy alg comparison to solve
        //need to create left and right arrays for final if

        int[] left = new int[n];
        Arrays.fill(left, 1); //fills each value as 1. Will update for less/more value in next loop
        int[] right = new int[n];
        Arrays.fill(right, 1);

        for(int i=1; i<n; i++){
            if(ratings[i]>ratings[i-1]){ //if the right-most value is > the left
                left[i] = left[i-1]+1; //Left child should have more candy than right child. So increment by 1
            }
        }

        for(int i=n-2; i>=0; i--){
            if(ratings[i]>ratings[i+1]){ //if the left-most value is > the right
                right[i] = right[i+1]+1; //Right child gets more candy than left. So increment down by 1
            }
        }

        for(int i=0; i<n; i++){
            candyCount += Math.max(left[i], right[i]);
        }
        return candyCount;
    }
}