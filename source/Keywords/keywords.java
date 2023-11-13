
package labset;

import java.util.Arrays;
import java.util.HashSet;
import java.util.Scanner;

public class keywords {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        HashSet<String> set = new HashSet<>();
        int n = sc.nextInt();
        sc.nextLine();
        for (int i = 0; i < n; i++) {
            String s = sc.nextLine();
            s = s.replace(" ", "-");
            set.add(s.toLowerCase());
        }
        System.out.println(set.size());
    }
}
