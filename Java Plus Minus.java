  import java.io.*;
  import java.math.*;
  import java.security.*;
  import java.text.*;
  import java.util.*;
  import java.util.concurrent.*;
  import java.util.regex.*;

  public class Solution {

      // Complete the plusMinus function below.
      static void plusMinus(int[] arr) {
          int total_count = arr.length;
          int positive_count = 0;
          int negative_count = 0;
          int zero_count = 0;

          for(int value: arr){
              if(value>0){
                  positive_count+=1;
              }
              else if(value<0){
                  negative_count+=1;
              }
              else{
                  zero_count+=1;
              }
          }



          System.out.println(String.format("%.6f", (float)positive_count/total_count));
          System.out.println(String.format("%.6f", (float)negative_count/total_count));
          System.out.println(String.format("%.6f", (float)zero_count/total_count));



      }

      private static final Scanner scanner = new Scanner(System.in);

      public static void main(String[] args) {
          int n = scanner.nextInt();
          scanner.skip("(\r\n|[\n\r\u2028\u2029\u0085])?");

          int[] arr = new int[n];

          String[] arrItems = scanner.nextLine().split(" ");
          scanner.skip("(\r\n|[\n\r\u2028\u2029\u0085])?");

          for (int i = 0; i < n; i++) {
              int arrItem = Integer.parseInt(arrItems[i]);
              arr[i] = arrItem;
          }

          plusMinus(arr);

          scanner.close();
      }
  }
