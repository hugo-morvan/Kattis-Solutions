
package kattis;

import java.util.*;
import java.util.stream.Collectors;


public class costumecontest {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
//        Map<String,Long> map = 
//        sc.tokens().limit(n)
//                .collect(Collectors.groupingBy(i->i,Collectors.counting()));
//        
//        System.out.println(map);
        
        TreeMap<String, Integer> treemap = new TreeMap<>();
        for (int i = 0; i < n; i++) {
            String name = sc.next();
            int count = treemap.getOrDefault(name, 0) + 1;
            treemap.put(name, count);
        }
        
        
        Set<String> candidates = treemap.keySet();
        int minVotes = n+1;
        
        for (String cand : candidates) {
            minVotes = Math.min(minVotes, treemap.get(cand));
        }
        List<String> winner = new ArrayList<>();
        for (String cand : candidates) {
            if(treemap.get(cand)==minVotes) winner.add(cand);
        }
        winner.forEach(System.out::println);
    }
}
