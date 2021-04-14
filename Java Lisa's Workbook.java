  import java.io.*;
  import java.math.*;
  import java.security.*;
  import java.text.*;
  import java.util.*;
  import java.util.concurrent.*;
  import java.util.regex.*;

  public class Solution {

      // Complete the workbook function below.
      static int workbook(int n, int k, int[] arr) {
          int count=0;

          int chapter_number = 1;

          for(int i=0; i<arr.length; i++){
              int limit_number = arr[i];
              int number=0;
              int limit_count=0;
              while(number<limit_number){
                  if(limit_number-limit_count>=k){
                      for(int j=1; j<=k; j++){
                          number+=1;
                          limit_count+=1;
                      if(chapter_number==number){
                          count+=1;     
                      }   
                  }
                  chapter_number+=1;   
                  }
                  else{
                      for(int l=0; l<limit_number-limit_count; l++){
                          number+=1;
                          if(chapter_number==number){
                          count+=1;

                  }

                      }
                     chapter_number+=1; 
                  }




                  }




          }
          return count;
      }




      private static final Scanner scanner = new Scanner(System.in);

      public static void main(String[] args) throws IOException {
          BufferedWriter bufferedWriter = new BufferedWriter(new FileWriter(System.getenv("OUTPUT_PATH")));

          String[] nk = scanner.nextLine().split(" ");

          int n = Integer.parseInt(nk[0]);

          int k = Integer.parseInt(nk[1]);

          int[] arr = new int[n];

          String[] arrItems = scanner.nextLine().split(" ");
          scanner.skip("(\r\n|[\n\r\u2028\u2029\u0085])?");

          for (int i = 0; i < n; i++) {
              int arrItem = Integer.parseInt(arrItems[i]);
              arr[i] = arrItem;
          }

          int result = workbook(n, k, arr);

          bufferedWriter.write(String.valueOf(result));
          bufferedWriter.newLine();

          bufferedWriter.close();

          scanner.close();
      }
  }
