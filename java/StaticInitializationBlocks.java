import java.io.*;
import java.util.*;
import java.text.*;
import java.math.*;
import java.util.regex.*;

public class StaticInitializationBlocks {
    private static boolean flag = true;
    private static int B;
    private static int H;

    static {
        Scanner scan = new Scanner(System.in);
        B = scan.nextInt();
        H = scan.nextInt();

        if(B <= -100 || B >= 100 || H <= -100 || H >= 100) {
            flag = false;
            System.out.print("Should be included in the interval -100 and 100");
        }
    }

    public static void main(String[] args){
        if(flag){
            int area=B*H;
            System.out.print(area);
        }

    }//end of main

}//end of class

