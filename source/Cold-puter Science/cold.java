
package kattis;

import java.util.Scanner;

public class cold {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int count = 0;
        for (int i = 0; i < n; i++) {
            int temp = sc.nextInt();
            if(temp<0)count++;
        }
        System.out.println(count);
    }
}
