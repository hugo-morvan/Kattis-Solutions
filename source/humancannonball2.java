
package kattis;

import java.util.*;

public class humancannonball2 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        for (int i = 0; i < n; i++) {
            double velocity = sc.nextDouble();
            double angle = Math.toRadians(sc.nextDouble());
            double distance = sc.nextDouble();
            
            double lower = sc.nextDouble();
            
            double upper = sc.nextDouble();
            
            //time = xdistance / xvelocity
            // x velocity = initial velocity * cos(angle)
            
            double time = distance / (velocity * Math.cos(angle));
            double height = (velocity*time*Math.sin(angle))-(0.5*9.81*time*time);
            
            
            if(height>(lower+1) && height<(upper-1))System.out.println("Safe");
            else System.out.println("Not Safe");
        }
    }
}
