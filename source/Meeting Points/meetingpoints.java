package kattis;

import java.util.*;

public class meetingpoints {

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        HashMap<String, Integer> vectorCount = new HashMap<>();
        
        for (int i = 0; i < n; i++) {
            Vector v = new Vector(sc.nextInt(), sc.nextInt(), sc.nextInt(), sc.nextInt()); 
            String vName = v.print();   //Switching to a String to search more efficiently for duplicates (aka colinear vectors)

            if (vectorCount.containsKey(vName)) {    //if this vector is already in the list, that means we have parallel lines
                int count = (vectorCount.get(vName)) + 1;
                vectorCount.replace(vName, count);
            } else {
                vectorCount.put(vName, 1);
            }
        }
        long count = 0; //long is important because the maximum number f intersection is (n²-n)/2 -> (100000²-100000)/2 = 4,999,950,000
        int lines = 0; //count how many lines are already "drawn"
        Set<String> keys = vectorCount.keySet();
        for (String key : keys) {
            int colinear = vectorCount.get(key);
            for (int i = 0; i < colinear; i++) { 
                count += lines;  //Each new line adds a number of intersection corresponding to the # of lines already drawn
            }
            lines += colinear;
        }
        System.out.println(count);
    }

}

class Vector {

    int x1;
    int y1;
    int x2;
    int y2;
    int X;
    int Y;

    Vector(int a, int b, int c, int d) {
        x1 = a;
        y1 = b;
        x2 = c;
        y2 = d;
        X = x2 - x1;
        Y = y2 - y1;
    }
    public String print(){
        return X +"&"+Y;
    }
    public boolean isColinear( Vector b) {
           return (X*b.Y-b.X*Y == 0);
    }

}
