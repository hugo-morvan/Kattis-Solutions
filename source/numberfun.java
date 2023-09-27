
package kattis;

import java.util.*;

public class numberfun {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        for (int i = 0; i < n; i++) {
            double a = sc.nextInt();
            double b = sc.nextInt();
            double c = sc.nextInt();
            
            if(a+b==c||b+a==c)System.out.println("Possible");
            else if(a-b==c||b-a==c)System.out.println("Possible");
            else if(a*b==c)System.out.println("Possible");
            else if(a/b==c||b/a==c)System.out.println("Possible");
            else System.out.println("Impossible");
        }
    }
}
