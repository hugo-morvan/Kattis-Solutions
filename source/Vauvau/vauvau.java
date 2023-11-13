
package assignment1;

import java.util.Scanner;

public class vauvau {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int a = sc.nextInt();
        int b = sc.nextInt();
        int c = sc.nextInt();
        int d = sc.nextInt();
        
        int[] villager = new int[3];
        villager[0] = sc.nextInt();
        villager[1] = sc.nextInt();
        villager[2] = sc.nextInt();
        
        for (int i = 0; i < 3; i++) {
            if (dog(a,b,villager[i]) && dog(c,d,villager[i])) {
                System.out.println("both");
            }else if(dog(a,b,villager[i]) || dog(c,d,villager[i])){
                System.out.println("one");
            }else{
                System.out.println("none");
            }
        }
    }
    public static boolean dog(int bite, int calm, int time){
        boolean attacked;
        if(time%(calm+bite)<=bite &&time%(calm+bite)!=0 ) attacked=true;
        else attacked = false;
        return attacked;
    }
        
    }

