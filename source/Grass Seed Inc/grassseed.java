
package kattis;

import java.util.Scanner;

public class grassseed {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        double c = sc.nextDouble();
        int l = sc.nextInt();
        double area = 0;
        for (int i = 0; i < l; i++) {
            double w = sc.nextDouble();
            double h = sc.nextDouble();
            area += w*h;
        }
        System.out.println(c*area);
    }
}
