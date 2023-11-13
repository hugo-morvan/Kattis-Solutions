package kattis;

import java.util.ArrayList;
import java.util.Scanner;

public class NewClass {

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String word = sc.next();
        if (isUnique(word)) {
            System.out.println("1");
        } else {
            System.out.println("0");
        }
    }    
    

    public static boolean isUnique(String s) {
        ArrayList<Character> list = new ArrayList<>();
        for (char c : s.toCharArray()) {
            if (list.contains(c)) {
                return false;
            } else {
                list.add(c);
            }
        }
        return true;
    }
}
