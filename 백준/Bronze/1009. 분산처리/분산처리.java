import java.util.ArrayList;
import java.util.Scanner;

class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int t = sc.nextInt();
        for (int i = 0; i < t; i++) {
            long a = sc.nextLong();
            long b = sc.nextLong();
            long result = 1;
            for (int j = 0; j < b; j++) {
                result = result * a % 10;
            }
            System.out.println(result == 0 ? 10 : result);
        }
    }
}