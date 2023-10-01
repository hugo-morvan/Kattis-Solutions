package kattis;

import java.util.Scanner;

public class filip {

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String a = sc.next();

        String b = sc.next();
        String nstr = "";
        char ch;
        for (int i = 0; i < a.length(); i++) {
            ch = a.charAt(i); //extracts each character
            nstr = ch + nstr; //adds each character in front of the existing string
        }
        a = nstr;
        int ah = Integer.valueOf(a);
         nstr = "";
        
        for (int i = 0; i < b.length(); i++) {
            ch = b.charAt(i); //extracts each character
            nstr = ch + nstr; //adds each character in front of the existing string
        }
        b = nstr;
        int bh = Integer.valueOf(b);
        
        if(ah>bh)System.out.println(ah);
        else System.out.println(bh);
    }
}
