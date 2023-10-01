
package kattis;

import java.util.Scanner;

public class faktor {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        double a = sc.nextInt();
        int goal = sc.nextInt();
        int ans = 0;
        while(Math.ceil(ans/a)!=goal){
            ans++;
        }
        System.out.println(ans);
    }
}
