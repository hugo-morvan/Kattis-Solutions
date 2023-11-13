import java.util.*;

public class CommonFactors {
    static final int[] primes = {2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47};
    static List<Integer> primeFactors = new ArrayList<>();
    static long numerator = 0, denominator=1;
    public static void main(String[] args) {    
        long num = new Scanner(System.in).nextLong();        
        
        //best choices for denominator are:
        //   2*3     = 6
        //   2*3*5   = 30
        //   2*3*5*7 = 210
        for (int i = 0; i < primes.length; i++) {
            if(denominator*primes[i] > num) break;
            denominator *= primes[i];
            primeFactors.add(primes[i]);
        }
        
        //numerator is all the numbers divisible by any of its factors
        //however, double counting is a concern
        
        //Inclusion Exclusion Principle                                                                        
        // (30/2 + 30/3 + 30/5) - (30/(2*3) + 30/(3*5) + 30/(2*5)) + (30/(2*3*5))        
        int flip = 1;
        for(int numElements = 1; numElements <= primeFactors.size(); numElements++ ){
            numerator += flip * combinations(1L, numElements,0);  
            flip*=-1;
        }
        
        //gcd to reduce the fraction
        long gcd = GCD(numerator,denominator);
        long a = numerator/gcd;
        long b = denominator/gcd;
        System.out.println(a + "/" + b);
        
        
    }
    public static long GCD(long a, long b){
        if (b==0) return a;
        return GCD(b,a%b);
    }
    
    //sum all the combinations of primeFactors of size elements
    public static long combinations(long product, int size, int index){
        if(size == 0) return denominator/product;
        if(index >= primeFactors.size()) return 0;
        return combinations(product*primeFactors.get(index),size-1,index+1) //combs including current index
                + combinations(product,size,index+1);                       //combs excluding current index
    }
}
