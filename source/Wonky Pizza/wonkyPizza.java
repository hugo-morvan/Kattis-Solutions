import java.util.*;

public class wonkyPizza {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        double a = sc.nextDouble();
        double b = sc.nextDouble();
        int n = sc.nextInt();
        
        double PI = Math.PI;
        double totalArea;
        if(a==0) totalArea = PI*b*b;
        else totalArea = (Math.pow(2*PI*(a+b),3)-Math.pow(2*PI*(b),3))/(12*PI*PI*a);
        
        double areaPerSlice = totalArea / n ;
        double thetaInit = 0;
        double thetaFinal;
       
        for (int i = 0; i < n-1; i++) {
            if(a==0)thetaFinal = (2*areaPerSlice + thetaInit*b*b)/(b*b);
            else thetaFinal = (Math.cbrt(12*PI*PI*a*areaPerSlice+Math.pow(a*thetaInit+2*PI*b, 3))-2*PI*b)/a;
            System.out.println(thetaFinal);
            thetaInit = thetaFinal;
        }
    }
}