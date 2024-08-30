
class Solution:
    def trappingWater(self, arr,n):
        #Code here
        left_max=arr[0]
        right_max=arr[n-1]
        left_pointer=0
        right_pointer=n-1
        total_water = 0
        water_level = 0
        while(left_pointer<right_pointer):
            if(arr[left_pointer]>left_max):
                left_max=arr[left_pointer]
            if(arr[right_pointer]>right_max):
                right_max=arr[right_pointer]
            if(left_max<=right_max):
                water_level = left_max-arr[left_pointer]
                if(water_level>0):
                    total_water+=water_level
                left_pointer+=1
            else:
                water_level = right_max - arr[right_pointer]
                if(water_level > 0):
                    total_water+=water_level
                right_pointer-=1
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