package kattis;

import java.util.*;

public class competitivearcadebasketball {

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int p = sc.nextInt();
        int m = sc.nextInt();
        TreeMap<String, Integer> map = new TreeMap<>();

        for (int i = 0; i <= n; i++) { //creation of the candidates
            String name = sc.nextLine();
            int count = 0;
            map.put(name, count);
        }
        ArrayList<String> winList = new ArrayList<>();
        boolean winner = false;
        for (int i = 0; i < m; i++) { //reading of the votes
            String name = sc.next();
            int vote = sc.nextInt();
            int count = (map.get(name)) + vote;
            
            map.put(name, count);
            if (map.get(name) >= p && !winList.contains(name)) {
                winList.add(name);
                winner = true;
            }
        }
        for (String name : winList) { //winner announcment
            System.out.println(name + " wins!");
        }
        if (!winner) {
            System.out.println("No winner!");
        }
    }

}
