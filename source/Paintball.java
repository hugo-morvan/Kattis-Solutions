import java.util.*;
import java.io.*;
public class Paintball{

    public static Map<Integer, Integer> targets = new HashMap<>();
    public static List<List<Integer>> adjacencyList;
    public static void main(String[] args){
       
        Scanner sc = new Scanner(System.in);

        int numPlayers = sc.nextInt() + 1; //n
        int numSightings = sc.nextInt(); //m

        adjacencyList = new ArrayList<>();
        for (int i = 0; i < numPlayers; i++) { // Initialize adjacency list
            adjacencyList.add(new ArrayList<>());
        }

        while (numSightings-- > 0) { // Read in sightings
            
            int a = sc.nextInt();
            int b = sc.nextInt();
            adjacencyList.get(a).add(b);
            adjacencyList.get(b).add(a);
        }

        for (int player = 0; player < numPlayers; player++) { 
            boolean[] hitPlayers = new boolean[numPlayers]; // Initialize array to keep track of which players have been hit
            for (int target : adjacencyList.get(player)) {
                if (playerHit(hitPlayers, target)) {
                    targets.put(target, player);
                    break;
                }
            }
        }

        if (targets.size() != (numPlayers - 1)) { // If there are not enough targets, print impossible
            System.out.println("Impossible");
            return;
        }

        for (int i = 1; i < numPlayers; i++) { // Print out the targets
            System.out.println(targets.get(i));
        }
    }

    public static boolean playerHit(boolean[] hitPlayers, int newTarget) { // Check if a player has been hit
        Integer player = targets.get(newTarget); // Get the player that is the target of the new target
        if (player == null) { // If the player is null, then the new target is not a target of anyone
            return true;
        }

        hitPlayers[newTarget] = true; // Mark the new target as hit
        for (int target : adjacencyList.get(player)) { // Check if the player's target has been hit
            if (!hitPlayers[target] && playerHit(hitPlayers, target)) { // If the player's target has not been hit, check if the player's target's target has been hit
                targets.put(target, player);
                return true;
            }
        }
        return false;
    }   
}
