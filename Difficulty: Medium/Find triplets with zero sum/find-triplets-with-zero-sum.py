#User function Template for python3

class Solution:
    #Function to find triplets with zero sum.    
    def findTriplets(self, arr, n):
        #code here
        arr.sort()
        j = n-1
        for i in range(n):
            j = i+1
            k = n-1
            while(j<k):
                sum = arr[i]+arr[j]+arr[k]
                if(sum==0):
                    return 1
                elif(sum>0):
                    k-=1
                else:
                    j+=1
        else:
            return 0
            
            


#{ 
 # Driver Code Starts
#Initial Template for Python 3

import atexit
import io
import sys

_INPUT_LINES = sys.stdin.read().splitlines()
input = iter(_INPUT_LINES).__next__
_OUTPUT_BUFFER = io.StringIO()
sys.stdout = _OUTPUT_BUFFER


@atexit.register
def write():
    sys.__stdout__.write(_OUTPUT_BUFFER.getvalue())


if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        n = int(input())
        a = list(map(int, input().strip().split()))
        if (Solution().findTriplets(a, n)):
            print(1)
        else:
            print(0)

# } Driver Code Ends