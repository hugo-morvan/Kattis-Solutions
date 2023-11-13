
package kattisProblems;

import java.util.*;
public class ABC {

    public static void main(String[] args) {
        
        Scanner sc = new Scanner(System.in);
        int[] num = new int[3];
        int a = sc.nextInt();
        num[0]=a;
        int b = sc.nextInt();
        num[1]=b;
        int c = sc.nextInt();
        num[2]=c;
        Arrays.sort(num);
       
        
        ArrayList<Character> let = new ArrayList<>();
        //ArrayList<Integer> num = new ArrayList<>();
        //num.add(sc.nextInt());
        //num.add(sc.nextInt());
        //num.add(sc.nextInt());
        
        
        
        String str = sc.next();
        let.add(str.charAt(0));
        let.add(str.charAt(1));
        let.add(str.charAt(2));
        
        for(char z: let){
            if(z == 'A'){
                System.out.print(num[0]+" ");
            }else if(z == 'B'){
                System.out.print(num[1]+" ");
            }else if(z=='C'){
                System.out.print(num[2]+" ");
            }
        }
        
        
    }
}

