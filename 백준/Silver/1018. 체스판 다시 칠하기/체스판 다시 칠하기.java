import java.util.Scanner;
import java.util.Arrays;

class Main {
    public static int compare(String[] oneSeq, String[] wFirst, String[] bFirst) {
        int wError = 0;
        int bError = 0;
        for (int i = 0; i < 8; i++) {
            for (int j = 0; j < 8; j++) {
                if (oneSeq[i].charAt(j) != wFirst[i].charAt(j)) {
                    wError++;
                } else {
                    bError++;
                }
            }
        }

        return wError < bError ? wError : bError;
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String[] wFirst = new String[8];
        String[] bFirst = new String[8];
        for (int i = 0; i < 8; i++) {
            if (i % 2 == 0) {
                wFirst[i] = "WBWBWBWB";
                bFirst[i] = "BWBWBWBW";
            } else if (i % 2 == 1) {
                bFirst[i] = "WBWBWBWB";
                wFirst[i] = "BWBWBWBW";
            }
        }
        int n = sc.nextInt();
        int m = sc.nextInt();
        String[] inputList = new String[n];
        int[] scores = new int[(n - 7) * (m - 7)];
        int seq = 0;

        for (int p = 0; p < n; p++) {
            inputList[p] = sc.next();
        }
        for (int i = 0; i <= n - 8; i++) { // i <= 9 - 8까지 //1 // 2번반복
            for (int j = 0; j <= m - 8; j++) {
                String[] oneSeq = { inputList[i].substring(0 + j, 8 + j), inputList[i + 1].substring(0 + j, 8 + j),
                        inputList[i + 2].substring(0 + j, 8 + j), inputList[i + 3].substring(0 + j, 8 + j),
                        inputList[i + 4].substring(0 + j, 8 + j),
                        inputList[i + 5].substring(0 + j, 8 + j), inputList[i + 6].substring(0 + j, 8 + j),
                        inputList[i + 7].substring(0 + j, 8 + j) };
                scores[seq] = compare(oneSeq, wFirst, bFirst);
                seq++;
            }

        }
        Arrays.sort(scores);
        System.out.println(scores[0]);

    }
}