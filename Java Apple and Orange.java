  import java.io.*;
  import java.math.*;
  import java.security.*;
  import java.text.*;
  import java.util.*;
  import java.util.concurrent.*;
  import java.util.regex.*;

  public class Solution {

      // Complete the countApplesAndOranges function below.
      static void countApplesAndOranges(int s, int t, int a, int b, int[] apples, int[] oranges) {
          int apple_distance = 0;
          int orange_distance = 0;
          int apple_count = 0;
          int orange_count = 0;

          for(int apple:apples){
              apple_distance= a+apple;
              if(apple_distance>=s && apple_distance<=t){
                  apple_count+=1;
              }
          }

          for(int orange:oranges){
              orange_distance= b+orange;
              if(orange_distance>=s && orange_distance<=t){
                  orange_count+=1;
              }
          }

          System.out.println(apple_count);
          System.out.println(orange_count);

      }

      private static final Scanner scanner = new Scanner(System.in);

      public static void main(String[] args) {
          String[] st = scanner.nextLine().split(" ");

          int s = Integer.parseInt(st[0]);

          int t = Integer.parseInt(st[1]);

          String[] ab = scanner.nextLine().split(" ");

          int a = Integer.parseInt(ab[0]);

          int b = Integer.parseInt(ab[1]);

          String[] mn = scanner.nextLine().split(" ");

          int m = Integer.parseInt(mn[0]);

          int n = Integer.parseInt(mn[1]);

          int[] apples = new int[m];

          String[] applesItems = scanner.nextLine().split(" ");
          scanner.skip("(\r\n|[\n\r\u2028\u2029\u0085])?");

          for (int i = 0; i < m; i++) {
              int applesItem = Integer.parseInt(applesItems[i]);
              apples[i] = applesItem;
          }

          int[] oranges = new int[n];

          String[] orangesItems = scanner.nextLine().split(" ");
          scanner.skip("(\r\n|[\n\r\u2028\u2029\u0085])?");

          for (int i = 0; i < n; i++) {
              int orangesItem = Integer.parseInt(orangesItems[i]);
              oranges[i] = orangesItem;
          }

          countApplesAndOranges(s, t, a, b, apples, oranges);

          scanner.close();
      }
  }
