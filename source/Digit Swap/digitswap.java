
package kattis;

import java.util.Scanner;

public class digitswap {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String n = sc.next();
        System.out.println(n.charAt(1)+""+n.charAt(0));
    }
}
