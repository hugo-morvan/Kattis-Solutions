
package kattis;

import java.util.Scanner;

public class chanukah {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int p = sc.nextInt();
        for (int i = 1; i <= p; i++) {
            int k = sc.nextInt();
            int n = sc.nextInt();
            int count = n;
            for (int j = 1; j <= n; j++) {
                count+=j;
            }
            System.out.println(k + " " + count);
        }
    }
}
