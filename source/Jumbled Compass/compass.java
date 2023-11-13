
package kattis;

import java.util.*;

public class compass {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int now = sc.nextInt();
        int correct = sc.nextInt();
        int cw, ccw;
        if(now<=correct){
            cw = correct-now;
            ccw = correct-(now+360);
        }
        else{
            cw = (correct+360)-now;
            ccw = correct-now;
        }
        if(Math.abs(cw)<=Math.abs(ccw))System.out.println(cw);
        else System.out.println(ccw);
    }
}
