
package kattis;

import java.util.*;

public class GCD {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        long a = sc.nextInt();
        long b = sc.nextInt();
        System.out.println(recEuclide(a,b));
    }
    public static long recEuclide(long a, long b){
        if(b == 0) return a;
        return recEuclide(b, a%b);
    }
}
