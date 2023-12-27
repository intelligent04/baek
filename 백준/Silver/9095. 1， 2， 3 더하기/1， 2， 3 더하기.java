import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int T = sc.nextInt();

        for (int i = 0; i < T; i++) {
            int n = sc.nextInt();
            int[] dp = new int[n + 1];

            // 초기값 설정
            dp[0] = 1;

            // 동적 계획법을 사용하여 경우의 수 계산
            for (int j = 1; j <= n; j++) {
                if (j - 1 >= 0)
                    dp[j] += dp[j - 1];
                if (j - 2 >= 0)
                    dp[j] += dp[j - 2];
                if (j - 3 >= 0)
                    dp[j] += dp[j - 3];
            }

            // 결과 출력
            System.out.println(dp[n]);
        }
    }
}
