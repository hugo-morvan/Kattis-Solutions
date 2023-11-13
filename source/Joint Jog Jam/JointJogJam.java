
package kattis;

import java.util.Scanner;

public class JointJogJam {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int x1i = sc.nextInt();
        int y1i = sc.nextInt();
        int x2i = sc.nextInt();
        int y2i = sc.nextInt();
        
        int x1f = sc.nextInt();
        int y1f = sc.nextInt();
        int x2f = sc.nextInt();
        int y2f = sc.nextInt();
        
        double di = Math.sqrt((x2i-x1i)*(x2i-x1i)+(y2i-y1i)*(y2i-y1i));
        double df = Math.sqrt((x2f-x1f)*(x2f-x1f)+(y2f-y1f)*(y2f-y1f));
        
        if(di>=df) System.out.println(di);
        else System.out.println(df);
    }
    
}
