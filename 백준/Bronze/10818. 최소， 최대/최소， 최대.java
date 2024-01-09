import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int t  = sc.nextInt();
        int max = -1000000;
        int min = 1000000;

        for(int i = 0; i <t; i++) {
            int temp = sc.nextInt();
            if (temp>max) max = temp;
            if (temp<min) min = temp;
        }
        System.out.printf("%d %d%n",min,max);
       
        
    }
}
