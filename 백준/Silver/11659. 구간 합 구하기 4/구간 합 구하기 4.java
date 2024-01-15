import java.util.Scanner;

public class Main {

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int m = sc.nextInt();
        Long[] arr = new Long[n+1];
        arr[0] = 0L;
        for (int i = 1; i <= n; i++) {
            arr[i] = arr[i - 1] + sc.nextLong();
        }
        for (int i = 0; i < m; i++) {
            int start = sc.nextInt();
            int end = sc.nextInt();
            System.out.println(arr[end] - arr[start - 1]);
        }
    }
}