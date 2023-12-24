import java.util.ArrayList;
import java.util.Scanner;

class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        String line = sc.next();
        double sum = 0.0;
        for (int i = 0; i < n; i++) {
            sum += ((line.charAt(i) - 96.0) * Math.pow(31, i));
        }
        System.out.println((long) sum);

    }
}