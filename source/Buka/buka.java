
package kattis;

import java.util.*;
import java.math.BigInteger;
public class buka {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        BigInteger A = new BigInteger(sc.next());
        String op = sc.next();
        BigInteger B = new BigInteger(sc.next());
        if(op.equals("+")) System.out.println(A.add(B));
        else System.out.println(A.multiply(B));
    }
}
