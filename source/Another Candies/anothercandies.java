package labset;

import java.util.*;

public class anothercandies {

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int t = sc.nextInt();
        for (int i = 0; i < t; i++) {
            int kids = sc.nextInt();
            long sum = 0;
            for (int j = 0; j < kids; j++) {
               sum += sc.nextLong();
               if(sum > kids) sum %= kids;
            }
            if(sum==0 || sum == kids)System.out.println("YES");
            else System.out.println("NO");
        }
    }
}