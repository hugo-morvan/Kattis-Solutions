package kattis;

import java.util.*;

public class recount {

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        TreeMap<String, Integer> treemap = new TreeMap<>();

        while (true) {
            String name = sc.nextLine();
            if (name.equals("***")) {
                break;
            }
            int count = treemap.getOrDefault(name, 0) + 1;
            treemap.put(name, count);
        }
        Set<String> candidates = treemap.keySet();
        int maxVotes = 0;
        for (String cand : candidates) {
            maxVotes = Math.max(maxVotes, treemap.get(cand));
        }
        List<String> winner = new ArrayList<>();
        for (String cand : candidates) {
            if(treemap.get(cand)==maxVotes)winner.add(cand);
        }
        if(winner.size()==1){
            System.out.println(winner.get(0));
        }else{
            System.out.println("Runoff!");
        }
    }
}
