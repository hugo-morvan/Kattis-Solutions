package kattis;

import java.util.Scanner;

public class oddaevenb {

    public static void main(String[] args) {
        
        long[][] ar = new long[100][2];
        ar[0][0] = 1;
        ar[0][1] = 0;
        ar[1][0] = 0;
        ar[1][1] = 1;
        ar[2][0] = 2;
        ar[2][1] = 1;
        for (int i = 4; i <= 100; i++) {
            ar[i-1][0] = ar[i-2][1] + ar[i-3][0];
            ar[i-1][1] = ar[i-3][0]+ar[i-3][1];
        }
        
        
        
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        System.out.println((ar[n-1][0]+ar[n-1][1])%1000000007);
    }
}
