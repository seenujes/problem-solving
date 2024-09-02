#User function Template for python3

class Solution:
    def sieveOfEratosthenes(self, N):
    	#code here 
    	lis=[];
        for i in range(2,N+1):
            s=1;
            for j in range(2,int(i**0.5)+1):
                if(not(i%j)):
                    s = 0;
                    break;
            if(s):
               lis.append(i)
        return lis;

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int(input())
    for _ in range(t):
        N = int(input())
        ob = Solution()
        ans = ob.sieveOfEratosthenes(N)
        for i in ans:
            print(i, end=" ")
        print()
# } Driver Code Ends