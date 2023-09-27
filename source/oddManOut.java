package labset;

import java.util.Scanner;
import java.util.TreeSet;

public class LabSet {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        for (int i = 1; i <= n; i++) {
            int g = sc.nextInt();
            TreeSet<Integer> set = new TreeSet<>();
            for (int j = 0; j < g; j++) {
                int c = sc.nextInt();
                if(set.contains(c)){
                    set.remove(c);
                }else{
                    set.add(c);
                }
            }
            int answer = set.first();
            System.out.println("Case #" + i + ": "+answer);
        }
    }
    
}
