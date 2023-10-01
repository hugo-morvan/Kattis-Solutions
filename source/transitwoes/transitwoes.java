
package kattis;

import java.util.Arrays;
import java.util.Scanner;

public class transitwoes {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int s = sc.nextInt();
        int t = sc.nextInt();
        int n = sc.nextInt();
        int[] walk = new int[n+1];
        int[] ride = new int[n];
        int[] start = new int[n];
        
        for (int i = 0; i < n+1; i++) {
            walk[i] = sc.nextInt();
        }
        
        for (int i = 0; i < n; i++) {
            ride[i] = sc.nextInt();
        }
        
        for (int i = 0; i < n; i++) {
            start[i] = sc.nextInt();
        }
        
        
        int total = 0;
        
        for (int i = 0; i < n; i++) {
            total += walk[i];
           
            if(start[i]>total){
                total += (start[i]-total);
               
            }
            total+= ride[i];  
         
        }
        total += walk[(walk.length-1)];
        if(total<t-s)System.out.println("yes");
        else System.out.println("no");
    }
}
