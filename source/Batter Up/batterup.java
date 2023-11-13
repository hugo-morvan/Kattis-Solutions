
package kattis;

import java.util.ArrayList;
import java.util.Scanner;

public class batterup {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        ArrayList<Integer> list = new ArrayList<>();
        for (int i = 0; i < n; i++) {
            int a = sc.nextInt();
            if(a>=0) list.add(a);
        }
        double sum = 0;
        for(int z : list)sum+=z;
        System.out.println(sum/list.size());
    }
}
