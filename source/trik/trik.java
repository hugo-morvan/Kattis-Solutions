package kattis;

import java.util.Scanner;

public class trik {

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String s = sc.next();
        boolean[] cups = {true, false, false};
        for (char c : s.toCharArray()) {
            if (c == 'A') {
                boolean temp = cups[0];
                cups[0] = cups[1];
                cups[1] = temp;
            } else if (c == 'B') {
                boolean temp = cups[1];
                cups[1] = cups[2];
                cups[2] = temp;
            } else {
                boolean temp = cups[0];
                cups[0] = cups[2];
                cups[2] = temp;
            }
        }
        for (int i = 0; i < 3; i++) {
            if (cups[i]) {
                System.out.println(i + 1);
            }
        }

    }
}
