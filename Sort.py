import sys
import heapq
class Solution(object):
    def insertion(self,nums):
        if len(nums)<= 1:
            return nums
        for i in range(1,len(nums)):
            temp = nums[i]
            for j in range(i):
                 if nums[i]<nums[j]:
                     for k in range(i-1,j-1,-1):
                         nums[i] = nums[i-1]
                     nums[j] = temp

    def selection(self,nums):
        if len(nums) <= 1:
            return nums
        for i in range(len(nums)-1):
            mini = sys.maxint
            index = i
            for j in range(i,len(nums)):
                if nums[j]<mini:
                    mini = nums[j]
                    index = j
            nums[i],nums[index] = nums[index],nums[i]

    def bubble(self,nums):
        if len(nums) <= 1:
            return nums
        while(True):
            count = 0
            for i in range(len(nums)-1):
                if nums[i] > nums[i+1]:
                    nums[i],nums[i+1] = nums[i+1],nums[i]
                    count += 1
            if count == 0:
                break

    def heapsort(self,nums):
         if len(nums) <= 1:
            return nums
         def buildheap(b):
             for i in range((b+1)/2,0,-1):
                 j = i
                 child = 2*j
                 while child<=b+1:
                     if child<=b and nums[child-1]<nums[child]:
                         child += 1
                     if nums[j-1]< nums[child-1]:
                         nums[j-1],nums[child-1] = nums[child-1],nums[j-1]
                         j = child
                         child = 2*j
                     else:
                         break
         for i in range(len(nums)-1,0,-1):
             buildheap(i)
             nums[0],nums[i] = nums[i],nums[0]

    def merge(self,a,b):
        c = [0 for i in range(len(a)+len(b))]
        l1 = 0
        l2 = 0
        for i in range(len(c)):
            if l1>len(a)-1:
                c[i] = b[l2]
                l2 += 1
            elif l2>len(b)-1:
                c[i] = a[l1]
                l1 += 1
            elif a[l1] < b[l2]:
                c[i] = a[l1]
                l1 += 1
            else:
                c[i] = b[l2]
                l2 += 1
        return c

    def mergesort(self,nums):
        if len(nums) <= 1:
            return nums
        mid = len(nums)/2
        return self.merge(self.mergesort(nums[:mid]),self.mergesort(nums[mid:]))

solution = Solution()
nums = [-1,2,1,2,1,1,5,7,52,45,6,109,8,-23,5,4,-1]
print(solution.mergesort(nums))

