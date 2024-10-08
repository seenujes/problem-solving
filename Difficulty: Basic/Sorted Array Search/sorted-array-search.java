//{ Driver Code Starts
import java.io.*;
import java.lang.*;
import java.util.*;

class gfg {

    public static void main(String args[]) throws IOException {
        BufferedReader read = new BufferedReader(new InputStreamReader(System.in));
        int t = Integer.parseInt(read.readLine());

        while (t-- > 0) {
            String s[] = read.readLine().trim().split("\\s+");

            int n = Integer.parseInt(s[0]);
            int k = Integer.parseInt(s[1]);

            int arr[] = new int[n];

            String st[] = read.readLine().trim().split("\\s+");

            for (int i = 0; i < n; i++) {
                arr[i] = Integer.parseInt(st[i]);
            }

            Solution obj = new Solution();

            System.out.println(obj.searchInSorted(arr, n, k));
        }
    }
}
// } Driver Code Ends


class Solution {
    static int searchInSorted(int arr[], int N, int K) {
        // Your code here
        int left = 0;
        int right = N-1;
        while(left<=right){
            int mid = left + (right-left)/2;
            if(arr[mid]==K) return 1;
            else if(arr[mid]<K) left++;
            else{
                right--;
            }
        }
        return -1;
    }
}