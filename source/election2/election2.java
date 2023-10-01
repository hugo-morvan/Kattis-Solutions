package kattis;

import java.util.*;

public class election2 {

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        sc.nextLine();
        HashMap<String, String> candidates = new HashMap<>();
        for (int i = 0; i < n; i++) { //Candidates registration
            candidates.put(sc.nextLine(), sc.nextLine());
        }
        TreeMap<String, Integer> votes = new TreeMap<>();

        int m = sc.nextInt();
        sc.nextLine();
        for (int i = 0; i < m; i++) { //votes reading
            String vote = sc.nextLine();

            int count = (votes.getOrDefault(vote, 0)) + 1;
            votes.put(vote, count);

        }

        TreeSet<String> winner = new TreeSet<>();
        int max = votes.values().stream().max(Integer::compare).get();
        for (String key : candidates.keySet()) { //detection of one or more winners
            try {
                if (votes.get(key).equals(max)) {
                    winner.add(key);

                }
            } catch (Exception e) {

            }
        }
        if (winner.size() == 1) {
            System.out.println(candidates.get(winner.first()));
        } else {
            System.out.println("tie");
        }
    }
}
