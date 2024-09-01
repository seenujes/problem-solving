#User function Template for python3
class Solution:

	# Function to find maximum
	# product subarray
	def maxProduct(self,arr, n):
		# code here
		max_product = min(arr)
        prefix_sum = 1
        suffix_sum = 1
        
        for i in range(n):
            if prefix_sum == 0:
                prefix_sum = 1
            if suffix_sum == 0:
                suffix_sum = 1
            prefix_sum *= arr[i]
            suffix_sum *= arr[n - i -1]
            
            max_product = max(max_product, prefix_sum, suffix_sum)
            
        return int(max_product)


#{ 
 # Driver Code Starts
#Initial Template for Python 3



if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        n = int(input())
        arr = list(map(int, input().strip().split()))
        ob = Solution()
        ans = ob.maxProduct(arr, n)
        print(ans)
        tc -= 1

# } Driver Code Ends