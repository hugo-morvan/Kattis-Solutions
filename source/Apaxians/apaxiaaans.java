
package kattis;

import java.util.*;

public class apaxiaaans {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String s = sc.next();
        char[] c = s.toCharArray();
        ArrayList<Character> answer = new ArrayList<>();
        answer.add(c[0]);
        for (int i = 1; i < c.length; i++) {
            if(c[i]!= c[i-1]){
                answer.add(c[i]);
            }
        }
        answer.forEach(a -> System.out.print(a));
    }
}
