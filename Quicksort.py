class Solution(object):
    def quicksort(self, nums):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """

        def partition(low,high):
            if low >= high:
                return
            pivot = low
            i = low + 1
            j = high
            while(i <= j):
                if (nums[i]>nums[pivot]):
                   nums[i],nums[j] = nums[j],nums[i]
                   j -= 1
                else:
                    i += 1
            nums[pivot],nums[j] = nums[j],nums[pivot]
            partition(low,j-1)
            partition(j+1,high)
            return

        partition(0,len(nums)-1)
        return
solution = Solution()
nums = [7,1,2,8,9,10,1,15,298,1,2,-1]
solution.quicksort(nums)
print(nums)


