import java.util.Scanner;

class Main {

  public static void main(String[] args) {
    Scanner sc = new Scanner(System.in);
    int n = sc.nextInt();
    for (int i = 1; i <= n; i++) {
      int j = n - i;
      for (int p = 0; p < j; p++) {
        System.out.print(" ");
      }
      for (int pp = 0; pp < i; pp++) {
        System.out.print("*");
      }
      System.out.println();
    }
  }
}