
package kattis;

import java.util.*;

public class tabsandspaces {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        ArrayList<Integer> list = new ArrayList<>();
        //input reading
        int F = sc.nextInt();
        for (int i = 0; i < F; i++) {
            int L = sc.nextInt();
            for (int j = 0; j < L; j++) {
                list.add(sc.nextInt());
            }
        }
        
        int initCost = list.stream().reduce(0,Integer::sum); //calculates the initial cost
        
        TreeSet<Integer> candidates = new TreeSet<>(); // my list of all the uniq spaces used 
        //the solution is between the min and the max of the list
        candidates.addAll(list);
        
        int max = candidates.last();
        for (int i = 1; i < max; i++) {
            candidates.add(i);
        }
        if(candidates.contains(0))candidates.remove(0);
        
        int minCost=initCost;
        int optiTab = 1;
        for(int tab:candidates){ //to do in here : calculate the cost in bytes of the certain indent. the idea is that the solution is among the spaces used.
            int cost = 0;
            for(int space : list){
                
                cost += space/tab;
                cost += space%tab;
                //works if number of spaces matches tab space. Otherwise, needs to adds the cost by individual spaces
                //idea: modulo le tab space, puis add le remainder en single space
            }
            if(cost<minCost){
                minCost = cost;
                optiTab = tab;
            }
        }
        
        System.out.println(optiTab);
        System.out.println(initCost-minCost);
    }
    
}
