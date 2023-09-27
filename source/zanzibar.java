
package kattis;

import java.util.*;

public class zanzibar {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        for (int i = 0; i < n; i++) {
            int in = 0;
            int cur = sc.nextInt();
            while(cur!=0){
                int next = sc.nextInt();
                int dif = next - cur*2;
                if(dif>0){
                    in += dif;
                }
                cur = next;
            }
            System.out.println(in);
        }
    }
}
