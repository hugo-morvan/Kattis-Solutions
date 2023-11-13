
package kattis;

import java.util.Scanner;

public class shatteredcake {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int w = sc.nextInt();
        int n = sc.nextInt();
        int area = 0;
        for (int i = 0; i < n; i++) {
            area += sc.nextInt() * sc.nextInt();
        }
        System.out.println(area/w);
    }
}
