
package kattisProblems;

import java.util.Scanner;

public class TakeTwoStones {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        if(n%2==0){
            System.out.println("Bob");
        }else{
            System.out.println("Alice");
        }
    }
}
