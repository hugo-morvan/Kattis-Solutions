
package kattis;

import java.util.Scanner;

public class ratingproblems {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        float n = sc.nextInt();
        float k = sc.nextInt();
        float tot = 0;
        for (int i = 0; i < k; i++) {
            tot += sc.nextInt();
        }
        float lowAvg = (tot + (n-k)*(-3))/n;
        System.out.println( lowAvg);
        float highAvg = (tot + (n-k)*(3))/n;
        System.out.println( highAvg);
    }
}
