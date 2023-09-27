
package kattis;

import java.util.Scanner;

public class tarifa {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int dataNew = sc.nextInt();
        int n = sc.nextInt();
        int dataLeft = dataNew;
        for (int i = 0; i < n; i++) {
            dataLeft = dataLeft - sc.nextInt() + dataNew;
        }
        System.out.println(dataLeft);
    }
}
