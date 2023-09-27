
package kattis;

import java.util.Scanner;

public class lastfactorialdigit {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        for (int i = 0; i < n; i++) {
            int f = sc.nextInt();
            int m = 1;
            for (int j =1 ; j <= f; j++) {
                m*=j;
            }
            String s = String.valueOf(m);
            System.out.println(s.charAt(s.length()-1));
        }
    }


}
