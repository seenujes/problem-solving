
class Solution:
    def trappingWater(self, arr,n):
        #Code here
        right_max=arr[n-1]
        left_max=arr[0]
        left_pointer=0
        right_pointer=n-2
        total_water=0
        while left_pointer<=right_pointer:
            if(left_max<arr[left_pointer]):
                left_max=arr[left_pointer]
            if(right_max<arr[right_pointer]):
                right_max=arr[right_pointer]
            if(left_max<right_max):
                water=left_max-arr[left_pointer]
                if(water>0):
                    total_water +=water
                left_pointer +=1
            else:
                water=right_max-arr[right_pointer]
                if(water>0):
                    total_water +=water
                right_pointer -=1
                
        return total_water

#{ 
 # Driver Code Starts
#Initial Template for Python 3

import math



def main():
        T=int(input())
        while(T>0):
            
            n=int(input())
            
            arr=[int(x) for x in input().strip().split()]
            obj = Solution()
            print(obj.trappingWater(arr,n))
            
            
            T-=1


if __name__ == "__main__":
    main()



# } Driver Code Ends