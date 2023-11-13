
package kattis;

import java.util.*;

public class vaccineefficacy {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        double v = 0;
        double va = 0;
        double vb = 0;
        double vc = 0;
        double c = 0;
        double ca = 0;
        double cb = 0;
        double cc = 0;
        for (int i = 0; i < n; i++) {
            String s = sc.next();
            boolean vaccine = s.charAt(0)=='Y';
            if(vaccine){
                v++;
                if(s.charAt(1)=='Y')va++;
                if(s.charAt(2)=='Y')vb++;
                if(s.charAt(3)=='Y')vc++;
            }
            else{
                c++;
                if(s.charAt(1)=='Y')ca++;
                if(s.charAt(2)=='Y')cb++;
                if(s.charAt(3)=='Y')cc++;
            }
        }
        if(va/v>=ca/c)System.out.println("Not Effective");
        else{
            System.out.println(((ca/c)-(va/v))/(ca/c)*100.00);
        }
         if(vb/v>=cb/c)System.out.println("Not Effective");
        else{
            System.out.println(((cb/c)-(vb/v))/(cb/c)*100.00);
        }
          if(vc/v>=cc/c)System.out.println("Not Effective");
        else{
            System.out.println(((cc/c)-(vc/v))/(cc/c)*100.00);
        }
    }
}
