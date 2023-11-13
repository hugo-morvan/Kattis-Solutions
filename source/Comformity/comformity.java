
package kattis;

import java.util.*;

public class comformity {
    public static void main(String[] args) {
        
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        TreeMap<String,Integer> map = new TreeMap<>();
        for (int i = 0; i < n; i++) {
            TreeSet<Integer> set = new TreeSet<>();
            for (int j = 0; j < 5; j++) {
                set.add(sc.nextInt());
            }
            
            int count = (map.getOrDefault(set.toString(), 0))+1;
            map.put(set.toString(), count);
        }
        Set<String> tot = map.keySet();
        int count=0;
        int max = map.values().stream().max(Integer::compare).get();
        for(String s : tot){
            if(map.get(s)== max){
                count+=map.get(s);
            }
        }System.out.println(count);
       // map.values().stream().max(Integer::compare).get();
        
        
    }
}
