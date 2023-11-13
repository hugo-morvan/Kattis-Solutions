
package labset;

import java.util.Scanner;
import java.util.TreeSet;

public class shoppinglist {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int m = sc.nextInt();
        TreeSet<String> uniq = new TreeSet<>();
        for (int i = 0; i < m; i++) {
            uniq.add(sc.next());
        }
        for (int i = 0; i < n-1; i++) {
            TreeSet<String> temp = new TreeSet<>();
            for (int j = 0; j < m; j++) {
                temp.add(sc.next());
            }
            uniq.retainAll(temp);
        }
        System.out.println(uniq.size());
        uniq.forEach(System.out::println);
    }
}
