  import java.io.*;
  import java.math.*;
  import java.text.*;
  import java.util.*;
  import java.util.regex.*;

  public class Solution {

      /*
       * Complete the timeConversion function below.
       */
      static String timeConversion(String s) {
          /*
           * Write your code here.
           */
           String time = s.substring(s.length()-2,s.length());
           String hour = s.substring(0,2);
           String result = "";


           if(hour.equals("12") && time.equals("AM")){
               result = s.replace("12","00");
               result = result.replace("AM","");
           }
           else if(!hour.equals("12") && time.equals("AM")){
               result = s.replace("AM","");
           }
           else if(hour.equals("12") && time.equals("PM")){
               result = s.replace("PM","");
           }
           else if(!hour.equals("12") && time.equals("PM")){
               int real_hour =  Integer.valueOf(hour);
               real_hour+=12;
               String final_hour = Integer.toString(real_hour);
               result = s.replace(hour,final_hour);
               result = result.replace("PM","");
           }
           return result;





      }

      private static final Scanner scan = new Scanner(System.in);

      public static void main(String[] args) throws IOException {
          BufferedWriter bw = new BufferedWriter(new FileWriter(System.getenv("OUTPUT_PATH")));

          String s = scan.nextLine();

          String result = timeConversion(s);

          bw.write(result);
          bw.newLine();

          bw.close();
      }
  }
