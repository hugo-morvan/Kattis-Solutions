
package labset;

import java.util.HashSet;
import java.util.Scanner;

public class securedoors {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        HashSet<String> hset = new HashSet<>();
        for (int i = 0; i < n; i++) {
            String key = sc.next();
            String name = sc.next();
            if(key.equals("entry")&& !hset.contains(name)){ //regular entry
                hset.add(name);
                System.out.println(name + " entered");
            }else if(key.equals("entry") && hset.contains(name)){//irregular entry
                
                System.out.println(name + " entered (ANOMALY)");
            }else if(key.equals("exit") && hset.contains(name)){ //regular exit
                hset.remove(name);
                System.out.println(name + " exited");
            }else if(key.equals("exit") && !hset.contains(name)){ //irregular exit
                
                System.out.println(name + " exited (ANOMALY)");
            }
        }
    }
}
