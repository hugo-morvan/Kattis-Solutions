package kattis;

import java.util.Scanner;

public class conquestcampaign {

    
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int r = sc.nextInt();
        int c = sc.nextInt();
        int n = sc.nextInt();
        int[][] grid = new int[r][c]; 
        //2 is for a conquered cell
        //1 is for a cell adjacent to a conquered cell
        //0 is for a cell not adjacent to a conquered cell
        for (int i = 0; i < n; i++) { //gives value 2 to the weak cells
            grid[sc.nextInt() - 1][sc.nextInt() - 1] = 2;
        }

        int day = 1;

        while (!isConqComplete(grid)) {
            
            //updates the board gives value 2 to the 1s
            for (int i = 0; i < r; i++) {  
                for (int j = 0; j < c; j++) {
                    if (grid[i][j] == 1) {
                        grid[i][j] = 2;
                    }
                }
            }
            //gives the value 1 to the adjacent of 2
            for (int i = 0; i < r; i++) {
                for (int j = 0; j < c; j++) {
                    if (grid[i][j] == 2) {
                        if (i > 0 && grid[i - 1][j] == 0) grid[i - 1][j] = 1; //up
                        if (i < r - 1 && grid[i + 1][j] == 0) grid[i + 1][j] = 1; //down
                        if (j > 0 && grid[i][j - 1] == 0) grid[i][j - 1] = 1; //left
                        if (j < c - 1 && grid[i][j + 1] == 0) grid[i][j + 1] = 1; //right
                    }
                }
            }
            day++;
        }
        System.out.println(day);
        sc.close();
    }
    
    public static boolean isConqComplete(int[][] grid) {
        //returns true/false if the board is completely conquered or not
        for (int[] row : grid) for (int val : row) {
            if (val == 0) return false;
        }
        return true;
    }
}
