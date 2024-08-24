//{ Driver Code Starts
import java.io.*;
import java.util.*;

class GFG {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int t;
        t = Integer.parseInt(br.readLine());
        while(t-- > 0){
            
            int a;
            a = Integer.parseInt(br.readLine());
            
            
            int b;
            b = Integer.parseInt(br.readLine());
            
            Solution obj = new Solution();
            int res = obj.gcd(a, b);
            
            System.out.println(res);
            
        }
    }
}

// } Driver Code Ends



class Solution {
    public static int gcd(int a, int b) {
        // code here
        int max = 1;
        int iterate = Math.min(a,b);
        while(b!=0){
            int temp = b;
            b = a%b;
            a = temp;
        }
        // for(int i=1;i<=iterate;i++){
        //     if(a%i==0 && b%i==0){
        //         max = i;
        //     }
        // }
        return a;
    }
}
        
