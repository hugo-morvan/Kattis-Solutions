//code by Zachary Tschetter

import java.util.*;
public class Nikola{
    public static void main(String[] args) throws Exception{
        Scanner sc = new Scanner(System.in);
        //read in
        int n = sc.nextInt();
        int[] cost = sc.tokens().limit(n).mapToInt(Integer::parseInt).toArray();
        
        //initialized 2d dp array with INFINITIES
        //rows are prev jump distance, columns are square index
        int[][] dp = new int[n][n];
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                dp[i][j] = Integer.MAX_VALUE;
            }
        }
        //starting square is free
        dp[0][0] = 0;
        
        //Our current cells value comes from a prev row (jump)
        //OR a larger column (square)
        //jumps from 0 to n, squares from n to 0
        for (int jump = 0; jump < n; jump++) {
            for (int square = n-1; square >= 0; square--) {
                if(dp[jump][square] == Integer.MAX_VALUE) continue;
                int small = square-jump;
                int big = square+jump+1;
                //if small is in range and we found a cheaper way to it, update it
                if(small >= 0 && dp[jump][small] > dp[jump][square]+cost[small]){
                    dp[jump][small] = dp[jump][square]+cost[small];
                }
                //if big is in range and we found a cheaper way to it, update it
                if(big < n && dp[jump+1][big] > dp[jump][square]+cost[big]){
                    dp[jump+1][big] = dp[jump][square]+cost[big];
                }
            }
            
        }
        
        //Find min of all end square costs
        int min = Integer.MAX_VALUE;
        for (int i = 0; i < n; i++) {
            min = Math.min(min, dp[i][n-1]);
        }
        System.out.println(min);
    }
}