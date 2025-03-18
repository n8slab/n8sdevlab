class Solution {
    public int canCompleteCircuit(int[] gas, int[] cost) {
        int answer = 0;
        int sum = 0;
        int gasCheck = 0;

        for(int i=0; i<gas.length; i++){
            sum += gas[i] - cost[i];
            gasCheck += gas[i] - cost[i];

            if(sum < 0){ //if there's not enough gas to get to next station
                sum = 0; //reset sum value to loop again
                answer = i+1; //Start from next station in index
            }
        }

        if(gasCheck<0){
            return -1;
        }else{
            return answer;
        }
    }
}