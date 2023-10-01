import java.util.*;
import java.math.*;
public class OverTheHill{
    public static void main(String[] args){
        Scanner input = new Scanner(System.in);
        int n = input.nextInt();
        int[][] encryptionMatrix = new int[n][n];
        for(int i = 0; i < n; i++){
            for(int j = 0; j < n; j++){
                encryptionMatrix[i][j] = input.nextInt();
            }
        }
        String buf = input.nextLine(); //to get to the next line
        String sentence = input.nextLine();
        //System.out.println("sentence: " + sentence);
        Hashtable<Character, Integer> coder = new Hashtable<Character, Integer>();
        coder.put('A',0);
        coder.put('B',1);
        coder.put('C',2);
        coder.put('D',3);
        coder.put('E',4);
        coder.put('F',5);
        coder.put('G',6);
        coder.put('H',7);
        coder.put('I',8);
        coder.put('J',9);
        coder.put('K',10);
        coder.put('L',11);
        coder.put('M',12);
        coder.put('N',13);
        coder.put('O',14);
        coder.put('P',15);
        coder.put('Q',16);
        coder.put('R',17);
        coder.put('S',18);
        coder.put('T',19);
        coder.put('U',20);
        coder.put('V',21);
        coder.put('W',22);
        coder.put('X',23);
        coder.put('Y',24);
        coder.put('Z',25);
        coder.put('0',26);
        coder.put('1',27);
        coder.put('2',28);
        coder.put('3',29);
        coder.put('4',30);
        coder.put('5',31);
        coder.put('6',32);
        coder.put('7',33);
        coder.put('8',34);
        coder.put('9',35);
        coder.put(' ',36);
        
        
        int[] preCrypted = new int[((int)Math.ceil(sentence.length()*1.0/n))*n]; //preCrypted is the sentence in numbers, but not encrypted
        //System.out.println(preCrypted.length);
        for(int i = 0; i < sentence.length(); i++){
            preCrypted[i] = coder.get(sentence.charAt(i));
        }
        for(int i = sentence.length(); i < preCrypted.length; i++){ //preCrypted is padded with 36's to make it a multiple of n
            preCrypted[i] = 36;
        }
        //System.out.println(preCrypted.length);
        int numBlocks = preCrypted.length/n; //number of blocks of n characters
        //System.out.println(numBlocks); // prints 0
        int[] encrypted = new int[preCrypted.length]; //encrypted is the sentence in numbers, but encrypted

        for(int i = 0; i < numBlocks; i++){ //for each block of n characters
            int[] block = new int[n]; 
            for(int j = 0; j < n; j++){       
                block[j] = preCrypted[i*n+j]; //put the character in the block
            }
            
            int[] encryptedBlock = new int[n]; //encryptedBlock is the block of n characters encrypted

            for(int j = 0; j < n; j++){ //matrix multiplication
                for(int k = 0; k < n; k++){
                    encryptedBlock[j] += encryptionMatrix[j][k]*block[k];
                }
                encryptedBlock[j] %= 37; //mod 37
            }
            for(int j = 0; j < n; j++){ //put the encrypted block back into the encrypted sentence
                encrypted[i*n+j] = encryptedBlock[j];
            }
        }
        
        String encryptedString = "";
        for(int i = 0; i < encrypted.length; i++){ //convert the encrypted sentence to a string using the coder
            for(Map.Entry<Character, Integer> entry : coder.entrySet()){
                if(entry.getValue() == encrypted[i]){
                    encryptedString += entry.getKey();
                }
            }
        }
        System.out.println(encryptedString);
        //System.out.println(encryptedString);
        input.close();
    }
}