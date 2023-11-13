
package kattis;

import java.util.Scanner;

public class different {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        while(sc.hasNextDouble()){
            double a = sc.nextDouble();
            double b = sc.nextDouble();
            System.out.println((long)Math.abs(a-b));
        }
    }
}
