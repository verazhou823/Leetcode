class Solution(object):
    def quicksort(self, nums,k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """

        def partition(low,high,k):
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
            if j == len(nums)-k:
                return j
            elif j > len(nums)-k:
                return partition(low,j-1,k)
            else:
                return partition(j+1,high,k)
        return nums[partition(0,len(nums)-1,k)]

solution = Solution()
nums = [7,1,2,8,9,10,1,15,298,1,2,-1]
print(solution.quicksort(nums,3))



