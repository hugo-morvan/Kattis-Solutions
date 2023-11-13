
package assignment1;

import java.util.ArrayList;
import java.util.Scanner;

public class greetings2 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String word = sc.next();
        char[] letters = word.toCharArray();
        
        for(char c : letters){
            if(c == 'e'){
                System.out.print("ee");
            }else{
                System.out.print(c);
            }
        }
        
    }
}
