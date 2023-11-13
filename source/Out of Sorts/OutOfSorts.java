import java.util.*;
public class OutOfSorts{
    public static void main(String[] args){
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        long m = sc.nextInt();
        long a = sc.nextInt();
        long c = sc.nextInt();
        long x = sc.nextInt();

        long[] sequence = new long[n];
        for(int i = 0; i < n; i++){ //fill the sequence
            x = (a*x + c) % m;
            sequence[i] = x;
            //System.out.print(x+ " ");
        }
        long[] sorted = new long[n];
        for(int i = 0; i < n; i++){ //fill the sorted array
            sorted[i] = sequence[i];
        }
        Arrays.sort(sorted);
        
        
        //binary search through the sequence array to find each value in the sorted array
        int count = 0;
        for(int i = 0; i < n; i++){
            int low = 0;
            int high = n-1;
            //System.out.println("searching for: " + sequence[i]);
            while(low <= high){
                int mid = (low + high)/2;
                if(sorted[i] == sequence[mid]){
                    //System.out.print(sequence[i] + " was found at index " + mid + "\n");
                    count++;
                    break;
                }
                else if(sorted[i] < sequence[mid]){
                    high = mid - 1;
                }
                else{
                    low = mid + 1;
                }
            }
        }
        System.out.println(count);
        sc.close();
    }
}