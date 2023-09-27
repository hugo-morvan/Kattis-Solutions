
package kattis;

import java.math.BigInteger;
import java.util.*;

public class simpleaddition {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        BigInteger big1 = new BigInteger(sc.next());
        BigInteger big2 = new BigInteger(sc.next());
        System.out.println(big1.add(big2));
    }
}
