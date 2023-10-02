
package lab8proj;

import java.util.ArrayList;
import java.util.Scanner;

public class everywhere {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int testCase = sc.nextInt();
        int trips;
        String city;
        ArrayList<String> cities = new ArrayList<>();
        for(int i = 0; i < testCase; i++){
            trips = sc.nextInt();
            for(int j = 0; j < trips; j++){
                city = sc.next();
               if(!cities.contains(city)){
                   cities.add(city);
               }
   
            }System.out.println(cities.size());
            cities.clear();
        }
    }
}
