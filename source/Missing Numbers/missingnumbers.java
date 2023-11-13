package assignment1;

import java.util.ArrayList;
import java.util.Scanner;

public class missingnumbers {

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int[] list = new int[n];
        ArrayList<Integer> myArray = new ArrayList<>();
        ArrayList<Integer> correction = new ArrayList<>();
        for (int i = 0; i < n; i++) {
            list[i] = sc.nextInt();
            myArray.add(list[i]);
        }
        //to do : check if it starts by 1, then check if each number is +1 from the precedent, 
        //if yes, move onto the next one, if not, add that number to the list
        int last = list[n - 1];
        for (int i = 1; i < last; i++) {
            if (!myArray.contains(i)) {
                correction.add(i);
            }
        }
        if (correction.isEmpty()) {
            System.out.println("good job");
        } else {
            for (int x : correction) {
                System.out.print(x + " ");
            }
        }

    }
}
