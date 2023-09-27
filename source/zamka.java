
package kattis;

import java.util.*;

public class zamka {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int l = sc.nextInt();
        int d = sc.nextInt();
        int x = sc.nextInt();
        TreeSet<Integer> set = new TreeSet<>();
        for (int i = l; i <= d; i++) {
            if(sumDig(i) == x)set.add(i);
        }
        System.out.println(set.first());
        System.out.println(set.last());
    }
    public static int sumDig(int a){
        String s = String.valueOf(a);
        int sum = 0;
        for(char c : s.toCharArray() ){
            sum += Integer.valueOf(String.valueOf(c));
        }
        return sum;
    }
}
