class Solution {
    public int[] platesBetweenCandles(String s, int[][] queries) {
       int n = s.length();
        int[] leftCandle = new int[n];  // Stores the index of nearest left candle
        int[] rightCandle = new int[n]; // Stores the index ofnearest right candle 
        int[] platePrefixSum = new int[n]; // Prefix sum of plates ('*')

        // Step 1: Compute leftCandle
        int lastCandle = -1;
        for (int i = 0; i < n; i++) {
            if (s.charAt(i) == '|') lastCandle = i;
            leftCandle[i] = lastCandle;
        }

        // Step 2: Compute rightCandle
        lastCandle = -1;
        for (int i = n - 1; i >= 0; i--) {
            if (s.charAt(i) == '|') lastCandle = i;
            rightCandle[i] = lastCandle;
        }

        // Step 3: Compute prefix sum of plates
        int platesCount = 0;
        for (int i = 0; i < n; i++) {
            if (s.charAt(i) == '*') platesCount++;
            platePrefixSum[i] = platesCount;
        }

        // Step 4: Process each query efficiently
        int[] result = new int[queries.length];
        for (int i = 0; i < queries.length; i++) {
            int left = queries[i][0], right = queries[i][1];

            // Find the first candle >= left and the last candle <= right
            int leftBoundary = rightCandle[left];
            int rightBoundary = leftCandle[right];

            // If there are no candles or invalid range, result is 0
            if (leftBoundary == -1 || rightBoundary == -1 || leftBoundary >= rightBoundary) {
                result[i] = 0;
            } else {
                result[i] = platePrefixSum[rightBoundary] - platePrefixSum[leftBoundary];
            }
        }

        return result; 
    }
}