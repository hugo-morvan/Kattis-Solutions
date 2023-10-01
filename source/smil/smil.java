package kattis;

import java.util.*;

public class smil {

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String s = sc.nextLine();
        s=s.concat("aa");
        
        char[] chars = s.toCharArray();
        for (int i = 0; i < chars.length - 2; i++) {
            if (chars[i] == ':') {
                if (chars[i + 1] == ')') {
                    System.out.println(i);
                } else if (chars[i + 1] == '-') {
                    if (chars[i + 2] == ')') {
                        System.out.println(i);
                    }
                }
            } else if (chars[i] == ';') {
                if (chars[i + 1] == ')') {
                    System.out.println(i);
                } else if (chars[i + 1] == '-') {
                    if (chars[i + 2] == ')') {
                        System.out.println(i);
                    }
                }
            }
        }

    }
}
