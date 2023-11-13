
package kattis;

import java.util.Scanner;

public class oddecho {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        for (int i = 1; i <= n; i++) {
            String s = sc.next();
            if(i%2==1){
                System.out.println(s);
            }
        }
    }
}
