  import java.io.*;
  import java.math.*;
  import java.security.*;
  import java.text.*;
  import java.util.*;
  import java.util.concurrent.*;
  import java.util.function.*;
  import java.util.regex.*;
  import java.util.stream.*;
  import static java.util.stream.Collectors.joining;
  import static java.util.stream.Collectors.toList;

  class Result {

      /*
       * Complete the 'fairRations' function below.
       *
       * The function is expected to return a STRING.
       * The function accepts INTEGER_ARRAY B as parameter.
       */

      public static String fairRations(List<Integer> B) {
      // Write your code here
          int count=0;
          int[] array = new int[B.size()];

          int size=0;
          for(int value : B){

          array[size++] = value;
  }

          for(int i=0; i<array.length-1; i++){
              if(array[i]%2!=0){
                  array[i]+=1;
                  array[i+1]+=1;
                  count+=2;
              }
          }

          String result =  String.valueOf(count);

          for(int value: array){
              if(value%2!=0){
                  result="NO";
                  break;
              }
          }

          return result;




      }

  }

  public class Solution {
      public static void main(String[] args) throws IOException {
          BufferedReader bufferedReader = new BufferedReader(new InputStreamReader(System.in));
          BufferedWriter bufferedWriter = new BufferedWriter(new FileWriter(System.getenv("OUTPUT_PATH")));

          int N = Integer.parseInt(bufferedReader.readLine().trim());

          List<Integer> B = Stream.of(bufferedReader.readLine().replaceAll("\\s+$", "").split(" "))
              .map(Integer::parseInt)
              .collect(toList());

          String result = Result.fairRations(B);

          bufferedWriter.write(result);
          bufferedWriter.newLine();

          bufferedReader.close();
          bufferedWriter.close();
      }
  }
