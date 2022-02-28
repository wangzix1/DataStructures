###https://medium.com/@edward.zhou/leet-code-1060-missing-element-in-sorted-array-explained-python3-solution-a1277b6ce32b
class Solution:
    def missingElement(self, nums:List[int], k:int) -> int:
        def findMissingElement(left, right, newK):
            if left == right:
                return None
            if left+1 == right:
                return nums[left] + newK
            md = (left + right)//2
            totalMissing = (nums[md] - nums[left]) - (md-left)
            if newK > totalMissing:
                return findMissingElement(md, right, newK - totalMissing)
            else:
                return findMissingElement(left, md, newK)

        expected = (nums[-1] - nums[0] + 1)
        actual = len(nums)
        if expected - actual >= k:
            return findMissingElement(0, len(nums)-1, k)
        else:
            return nums[-1] + (k-(expected - actual))

    

