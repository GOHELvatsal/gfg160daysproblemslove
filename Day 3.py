class Solution:
    def reverseArray(self, arr):
        # code here
        for i in range(len(arr)//2):
            arr[i],arr[-i - 1] = arr[-i - 1], arr[i]
        
