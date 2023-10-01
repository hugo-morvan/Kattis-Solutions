
package kattis;

import java.util.*;

public class lastminute {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        long uniqA = sc.nextInt();
        long uniqB = sc.nextInt();
        long reuseA = sc.nextInt();
        long reuseB = sc.nextInt();
        
        if(reuseA!=0 && reuseB!=0) System.out.println(reuseA*reuseB+uniqA+uniqB);
        else if(reuseA!=0 && reuseB==0) System.out.println(uniqB);
        else if(reuseB!=0 && reuseA==0) System.out.println(uniqA);
        else System.out.println(Math.min(uniqA,uniqB));
    }
}
