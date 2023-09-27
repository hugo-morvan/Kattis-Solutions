
package kattisProblems;

import java.util.Scanner;

public class Planina {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        // n=1 > 9 3² = (2^1 + 1)²
        // n=2 > 25 5² = (2^2 + 1)²
        // n=3 > 81 9² = (2^3 +1)²
        int square = ((int)Math.pow(2, n)+1)*((int)Math.pow(2, n)+1);
        System.out.println(square);
    }
}
