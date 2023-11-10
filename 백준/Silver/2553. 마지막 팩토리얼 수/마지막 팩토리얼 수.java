        import java.util.Scanner;

class Main {

    static long facto(int n) {
        long factoSum = 1;
        for (int j = 2; j <= n; j++) {
            factoSum *= j;
            while (factoSum % 10 == 0)
                factoSum /= 10;
            factoSum %= 1000000000;

        }
        return factoSum;
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        long factoN = facto(n);
        
        while (true) {
            if (factoN % 10 != 0) {
                System.out.printf("%d", factoN % 10);
                break;
            } else
                factoN /= 10;
        }
        sc.close();

    }
}
        
                
