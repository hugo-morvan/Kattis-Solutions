
package review1;

import java.util.Scanner;


public class Elec {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int cases = sc.nextInt();
        int k = 0; 
        for(int i = 0; i < cases; i++){
            k = sc.nextInt();
            int o = 0;
            for(int j = 0; j<k; j++){
                o += sc.nextInt();
            }
            o = o - k + 1;
            System.out.println(o);
            
        }
    }
 
}
