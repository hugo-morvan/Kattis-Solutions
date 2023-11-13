package kattis;

import java.util.Scanner;

public class pot {

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        String[] list = new String[n];
        for (int i = 1; i <= n; i++) {
            list[i - 1] = sc.next();
        }
        int sum = 0;
        for (int i = 1; i <= n; i++) {
            String s = list[i - 1];
            int p = Integer.parseInt(s,s.length()-1,s.length(),10);
            int a = Integer.parseInt(s,0,s.length()-1,10);
            sum += Math.pow(a, p);
        }
        System.out.println(sum);
    }
}
