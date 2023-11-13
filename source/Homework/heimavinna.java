
package kattis;

import java.util.Scanner;

public class heimavinna {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String s = sc.next();
        String[] list = s.split(";");
        int count = 0;
        for(String a : list){
            if(a.contains("-")){
                String[] range = a.split("-");
                int b = Integer.parseInt(range[0]);
                int c = Integer.parseInt(range[1]);
                count+= c-b+1;
            }else{
                count++;
            }
        }System.out.println(count);
    }
}
