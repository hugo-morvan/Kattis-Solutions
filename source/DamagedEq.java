package kattisProblems;

import java.util.Scanner;

public class DamagedEq {

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int a = sc.nextInt(), b = sc.nextInt(), c = sc.nextInt(), d = sc.nextInt();
        boolean none = true;
        if (a * b == c * d) {
            System.out.println(a + " * " + b + " = " + c + " * " + d);
            none = false;
        }
        if (a * b == c + d) {
            System.out.println(a + " * " + b + " = " + c + " + " + d);
            none = false;
        }
        if (a * b == c - d) {
            System.out.println(a + " * " + b + " = " + c + " - " + d);
            none = false;
        }
        if (d != 0) {
            if (a * b == c / d) {
                System.out.println(a + " * " + b + " = " + c + " / " + d);
                none = false;
            }
        }

        if (a + b == c * d) {
            System.out.println(a + " + " + b + " = " + c + " * " + d);
            none = false;
        }
        if (a + b == c + d) {
            System.out.println(a + " + " + b + " = " + c + " + " + d);
            none = false;
        }
        if (a + b == c - d) {
            System.out.println(a + " + " + b + " = " + c + " - " + d);
            none = false;
        }
        if (d != 0) {
            if (a + b == c / d) {
                System.out.println(a + " + " + b + " = " + c + " / " + d);
                none = false;
            }
        }
        if (a - b == c * d) {
            System.out.println(a + " - " + b + " = " + c + " * " + d);
            none = false;
        }
        if (a - b == c + d) {
            System.out.println(a + " - " + b + " = " + c + " + " + d);
            none = false;
        }
        if (a - b == c - d) {
            System.out.println(a + " - " + b + " = " + c + " - " + d);
            none = false;
        }
        if (d != 0) {
            if (a - b == c / d) {
                System.out.println(a + " - " + b + " = " + c + " / " + d);
                none = false;
            }
        }
        if (b != 0) {
            if (a / b == c * d) {
                System.out.println(a + " / " + b + " = " + c + " * " + d);
                none = false;
            }
            if (a / b == c + d) {
                System.out.println(a + " / " + b + " = " + c + " + " + d);
                none = false;
            }
            if (a / b == c - d) {
                System.out.println(a + " / " + b + " = " + c + " - " + d);
                none = false;
            }
            if (d != 0) {
                if (a / b == c / d) {
                    System.out.println(a + " / " + b + " = " + c + " / " + d);
                    none = false;
                }
            }
        }
        if (none) {
            System.out.println("problems ahead");
        }
    }
}
