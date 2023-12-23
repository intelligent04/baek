import java.util.ArrayList;
import java.util.Scanner;

class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        Long a = sc.nextLong();
        Long b = sc.nextLong();
        Long c = sc.nextLong();
        int[] nums = new int[10];
        Long num = a * b * c;
        String numString = num.toString();
        for (int i = 0; i < numString.length(); i++) {
            int j = numString.charAt(i) - 48;
            nums[j]++;
        }
        for (int i = 0; i < 10; i++) {
            System.out.println(nums[i]);
        }
    }
}