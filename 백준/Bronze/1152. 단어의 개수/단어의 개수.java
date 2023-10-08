import java.util.Arrays;
import java.util.Scanner;

public class Main {

  public static void main(String[] args) {
    Scanner sc = new Scanner(System.in);
    String input = sc.nextLine();

    String[] arr = input.split(" ");
    int count = arr.length;
    //System.out.println(Arrays.toString(arr));

    if (arr.length >= 1) {
      if (arr.length == 1 & arr[0] == "")
        count += 1;
      if (arr[0] == "")
        count -= 1;
      if (arr[arr.length - 1] == "")
        count -= 1;

    }
    System.out.println(count);
    sc.close();

  }
}