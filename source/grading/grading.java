
package kattis;

import java.util.Scanner;

public class grading {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        
        int a = sc.nextInt();
        int b = sc.nextInt();
        int c = sc.nextInt();
        int d = sc.nextInt();
        int e = sc.nextInt();
        
        int grade  = sc.nextInt();
        
        if(grade>=a)System.out.println("A");
        else if(grade>=b)System.out.println("B");
        else if(grade>=c)System.out.println("C");
        else if(grade>=d)System.out.println("D");
        else if(grade>=e)System.out.println("E");
        else System.out.println("F");
    }
}
