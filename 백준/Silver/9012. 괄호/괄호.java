import java.util.ArrayList;
import java.util.Scanner;

class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int t = sc.nextInt();
        for (int i = 0; i < t; i++) {
            ArrayList<Character> li = new ArrayList<>();
            String line = sc.next();
            for (int j = 0; j < line.length(); j++) {
                li.add(line.charAt(j));
            }
            for (int j = 0; j < line.length(); j++) {
                for (int q = 0; q < li.size() - 1; q++) {
                    if (li.get(q) == '(' && li.get(q + 1) == ')') {
                        li.remove(q);
                        li.remove(q);
                    }
                }
            }
            if (li.isEmpty())
                System.out.println("YES");
            else
                System.out.println("NO");

        }
    }
}