
package kattis;

import java.util.Scanner;
import java.util.Set;
import java.util.TreeMap;
import java.util.TreeSet;

public class dicecup {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int m = sc.nextInt();
        TreeMap<Integer,Integer> map = new TreeMap<>();
        
        for (int i = 1; i <= n; i++) {
            for (int j = 1; j <= m; j++) {
                int count = (map.getOrDefault(i+j,0))+1;
           map.put(i+j, count);
            }
        }
        Set<Integer> val = map.keySet();
        int max = 0;
        
        for(int num : val){
            if(map.get(num)>max) max=map.get(num);
        }
        TreeSet<Integer> ans = new TreeSet<>();
        for(int num : val){
            if(map.get(num) == max){
                ans.add(num);
            }
        }
        ans.forEach(System.out::println);
    }
}
