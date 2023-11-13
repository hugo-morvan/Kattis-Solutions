
package icpc;

import java.util.*;

public class mult {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int targ = sc.nextInt();
        for (int i = 0; i < n-1; i++) {
            int curr = sc.nextInt();
            if(curr%targ==0){
                System.out.println(curr);
                targ= sc.nextInt();
                i++;
            }
        }
    }
}
