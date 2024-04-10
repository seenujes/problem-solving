#User function Template for python3
class Solution:
    def findKRotation(self,arr,  n):
        # code here
        low = 0
        ans=max(arr)
        index=-1
        high = n - 1
        while low <= high:
            mid = (low + high) // 2
            if(arr[low]<=arr[high]):
                if(arr[low]<ans):
                    index=low
                    ans=arr[low]
                break
             
            elif(arr[low]<=arr[mid]):
                if(arr[low]<ans):
                    index=low
                    ans=arr[low]
                low=mid+1
                
            else:
                if(arr[mid]<ans):
                    index=mid
                    ans=arr[mid]
                
                high=mid-1
        return index
                


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':

	tc=int(input())
	while tc > 0:
		n=int(input())
		a=list(map(int , input().strip().split()))
		ob = Solution()
		ans=ob.findKRotation(a, n)
		print(ans)
		tc=tc-1



# } Driver Code Ends