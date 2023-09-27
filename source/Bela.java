package kattis;
import java.util.*;
public class Bela {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        String suit = sc.next();
        int score = 0;
        for (int i = 0; i < n*4; i++) {
            String hand = sc.next();
            if(hand.charAt(1) == suit.charAt(0)){
                if(hand.charAt(0) == 'A') score += 11;
                if(hand.charAt(0) == 'K') score += 4;
                if(hand.charAt(0) == 'Q') score += 3;
                if(hand.charAt(0) == 'J') score += 20;
                if(hand.charAt(0) == 'T') score += 10;
                if(hand.charAt(0) == '9') score += 14;
                if(hand.charAt(0) == '8') score += 0;
                if(hand.charAt(0) == '7') score += 0;
            }else{
                if(hand.charAt(0) == 'A') score += 11;
                if(hand.charAt(0) == 'K') score += 4;
                if(hand.charAt(0) == 'Q') score += 3;
                if(hand.charAt(0) == 'J') score += 2;
                if(hand.charAt(0) == 'T') score += 10;
                if(hand.charAt(0) == '9') score += 0;
                if(hand.charAt(0) == '8') score += 0;
                if(hand.charAt(0) == '7') score += 0;
            }
        }
        System.out.println(score);   
    }
}
