#User function Template for python3

class Solution:
	def reverse_digit(self, n):
		# Code here
		a = str(n)
		b = a[::-1]
# 		for i in range(0,len(b)):
# 		    if(b[i]=="0"):
# 		        b[i].delete()
		
		return int(b.lstrip('0'))

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		n = int(input())
		ob = Solution();
		ans = ob.reverse_digit(n)
		print(ans)
# } Driver Code Ends