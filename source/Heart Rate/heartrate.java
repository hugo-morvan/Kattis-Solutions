
package kattis;

import java.util.Scanner;

public class heartrate {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        for (int i = 0; i < n; i++) {
            int b = sc.nextInt();
            double p = sc.nextDouble();
            System.out.print((60*b/p)-60/p + " ");
            System.out.print((60*b/p+ " "));
            System.out.println((60*b/p)+60/p);
        }
    }
}
