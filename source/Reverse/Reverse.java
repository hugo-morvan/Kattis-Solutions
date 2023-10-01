
package assignment1;

import java.util.Scanner;

public class Reverse {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int[] list = new int[n];
        for (int i = 0; i < n; i++) {
            list[i] = sc.nextInt();
        }
        for (int i = 0; i < n; i++) {
            System.out.println(list[(n-1)-i]);
        }
    }
}
