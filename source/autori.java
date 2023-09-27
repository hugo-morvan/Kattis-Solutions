
package kattis;

import java.util.*;

public class autori {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String s = sc.next();
        for(char c : s.toCharArray()){
            if( "AZERTYUIOPQSDFGHJKLMWXCVBN".contains(String.valueOf(c))) System.out.print(c);
        }
    }
}
