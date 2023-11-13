
package labset;

import java.util.HashSet;
import java.util.Scanner;

public class shiritori {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int player = 1;
        int loser = 0;
        String prev = sc.next();
        HashSet<String> set = new HashSet<>();
        set.add(prev);
        for (int i = 0; i < n-1; i++) {
            String s = sc.next();
            if(!set.contains(s) && (s.charAt(0) == prev.charAt(prev.length()-1))){ //valid entry
                set.add(s);
            }else{ //unvalid entry 
                loser = player;
                set.add(s);
                break;
            }
            prev = s;    
            player *= -1;
        }
        if (loser == 0) {
            System.out.println("Fair Game");
        }else if(loser == -1){
            System.out.println("Player 1 lost");
        }else if(loser == 1){
            System.out.println("Player 2 lost");
        }
    }
}
