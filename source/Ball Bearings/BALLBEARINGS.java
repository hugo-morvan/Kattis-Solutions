
package kattis;

import java.util.*;

public class BALLBEARINGS {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        for (int i = 0; i < n; i++) {
            double D = sc.nextDouble();
            double d = sc.nextDouble();
            double s = sc.nextDouble();
            
            int answer = 3;
            //double estimate = answer *( s +(d*Math.sin((Math.PI*(answer-2))/(2*answer))));
            //double exact = Math.PI*(D-d);
            
            while((answer*(D-d)*Math.sin(Math.PI/answer))/answer-d > s){
                answer++;
                
            }
            System.out.println((answer-1));
        }
    }
}
