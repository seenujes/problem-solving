#User function Template for python3


class Solution:
    def find(self, arr, n, x):
        
        # code here
        res=[]
        for i in range(n):
            if(arr[i]==x):
                res.append(i)
        if(x in arr):
            return res[0],res[len(res)-1]
        return (-1,-1)


#{ 
 # Driver Code Starts
t=int(input())
for _ in range(0,t):
    l=list(map(int,input().split()))
    n=l[0]
    x=l[1]
    arr=list(map(int,input().split()))
    ob = Solution()
    ans=ob.find(arr,n,x)
    print(*ans)
# } Driver Code Ends