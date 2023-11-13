
package kattis;

import java.util.Scanner;

public class lamps {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        double h = sc.nextInt();
        double p = sc.nextInt();
        double kInc = 5;
        double kLow = 60;
        int days = 0;
        while(kInc<kLow && (days*h<1000)){
            days++;
            kInc += (60*h*p/100000);
            kLow += (11*h*p/100000);
        }
        kInc+=5;
        while(kInc<kLow && (days*h<2000)){
            days++;
            kInc += (60*h*p/100000);
            kLow += (11*h*p/100000);
        }kInc+=5;
        while(kInc<kLow && (days*h<3000)){
            days++;
            kInc += (60*h*p/100000);
            kLow += (11*h*p/100000);
        }
        kInc+=5;
        while(kInc<kLow && (days*h<4000)){
            days++;
            kInc += (60*h*p/100000);
            kLow += (11*h*p/100000);
           
        }kInc+=5;
        while(kInc<kLow && (days*h<5000)){
            days++;
            kInc += (60*h*p/100000);
            kLow += (11*h*p/100000);
        }
        kInc+=5;
        while(kInc<kLow && (days*h<6000)){
            days++;
            kInc += (60*h*p/100000);
            kLow += (11*h*p/100000);
        }kInc+=5;
        while(kInc<kLow && (days*h<7000)){
            days++;
            kInc += (60*h*p/100000);
            kLow += (11*h*p/100000);
        }kInc+=5;
        while(kInc<kLow && (days*h<8000)){
            days++;
            kInc += (60*h*p/100000);
            kLow += (11*h*p/100000);
        }
        System.out.println(days);     
    }
}
