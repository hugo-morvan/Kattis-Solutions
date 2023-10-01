package kattis;

import java.util.Scanner;

public class Kattis {

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int height = 1;
        if (n == 1) {
            System.out.println("1");
        } else {
            while (((height * ((4 * height * height) - 1)) / 3) <= n) {
                height++;
            }
            System.out.println(height - 1);
        }
    }
}
