
package kattis;

import java.util.Scanner;

public class NewClass {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int a = sc.nextInt();
        int b = sc.nextInt();
        int c = sc.nextInt();
        int AB = b - a;
        int BC = c-b;
        if(AB>BC)System.out.println(AB-1);
        else System.out.println(BC -1);
        
    }
}
