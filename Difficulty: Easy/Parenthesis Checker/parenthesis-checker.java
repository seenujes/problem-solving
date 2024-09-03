//{ Driver Code Starts
import java.util.*;
import java.io.*;
import java.lang.*;

class Driverclass
{
    public static void main(String args[])
    {
        Scanner sc = new Scanner(System.in);
        
        //Reading total number of testcases
        int t= sc.nextInt();
        
        while(t-- >0)
        {
            //reading the string
            String st = sc.next();
            
            //calling ispar method of Paranthesis class 
            //and printing "balanced" if it returns true
            //else printing "not balanced"
            if(new Solution().ispar(st) == true)
                System.out.println("balanced");
            else
                System.out.println("not balanced");
        
        }
    }
}
// } Driver Code Ends



class Solution
{
    //Function to check if brackets are balanced or not.
    static boolean ispar(String x)
    {
        // add your code here
        // Stack stack = new Stack(x.length());
        Stack<Character> stack = new Stack<>();
        if(x.length()==1)return false;
        for(int i=0;i<x.length();i++){
            char a = x.charAt(i);
            if(a=='('||a=='{'||a=='['){
                stack.push(a);
            }
            else if(a==')'||a=='}'||a==']'){
                if(stack.isEmpty()) return false;
                char top =(char) stack.pop();
                if(
                (a==')' && top != '(') ||
                (a=='}' && top !='{')||
                (a==']' && top !='[')){
                    return false;
                }
            }
        }
        return stack.isEmpty();
        
    }
}
