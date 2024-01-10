import java.util.ArrayList;
import java.util.Collections;
import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int k = sc.nextInt();
        int seq = 0;
        int out = 0;
        ArrayList<Integer> li = new ArrayList<Integer>();
        for (int i = 0; i < n; i++) {
            li.add(sc.nextInt());
        }
        Collections.sort(li, Collections.reverseOrder());
        while (seq <= n - 1) {
            while (k - li.get(seq) >= 0) {
                k -= li.get(seq);
                out++;
            }
            seq++;
        }
        System.out.println(out);

    }
}
