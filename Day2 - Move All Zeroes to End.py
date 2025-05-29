class Solution:
	def pushZerosToEnd(self,arr):
    	non_Zero = 0
    	
    	for i in range(len(arr)):
    	    if arr[i] != 0:
    	        arr[non_Zero] = arr[i]
    	        non_Zero += 1
    	        
        for i in range(non_Zero, len(arr)):
            arr[i] = 0
