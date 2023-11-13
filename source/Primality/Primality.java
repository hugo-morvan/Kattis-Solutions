package kattis;

import java.util.*;
import java.math.*;
public class Primality{
    public static void main(String[] args){
        Scanner sc = new Scanner(System.in);
        System.out.println(BigInteger.valueOf(sc.nextLong()).isProbablePrime(5)?"YES":"NO");
    }
}