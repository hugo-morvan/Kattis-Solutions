
package kattis;

import java.util.Scanner;

public class theplank {
    public static void main(String[] args) {
        long[] ar = new long[24];
        ar[0] = 1;
        ar[1] = 2;
        ar[2] = 4;
        
        for (int i = 3; i < 24; i++) {
            ar[i]=ar[i-3]+ar[i-2]+ar[i-1];
        }
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        System.out.println(ar[n-1]);
        
    }
}
