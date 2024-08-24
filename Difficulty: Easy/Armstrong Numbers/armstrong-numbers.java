//{ Driver Code Starts
// Initial Template for Java
import java.io.*;
import java.util.*;

class GFG {
    public static void main(String args[]) throws IOException {
        BufferedReader read = new BufferedReader(new InputStreamReader(System.in));
        int t = Integer.parseInt(read.readLine());
        while (t-- > 0) {
            int n = Integer.parseInt(read.readLine());
            Solution ob = new Solution();

            System.out.println(ob.armstrongNumber(n));
        }
    }
}
// } Driver Code Ends


// User function Template for Java
class Solution {
    static String armstrongNumber(int n) {
        // code here
        int sum = 0;
        int value = 0;
        int originalvalue = n;
        while(n>0){
            value = n%10;
            sum = sum+(value*value*value);
            n =(n/10) ;
        }
        if(sum==originalvalue){
            return "true";
        }
        return "false";
        
    }
}